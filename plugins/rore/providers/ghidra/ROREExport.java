// RORE-owned headless GhidraScript. Observations are derived from the imported program.
// @category RORE

import java.io.File;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.util.HexFormat;
import java.util.Set;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.util.headless.HeadlessScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.address.AddressIterator;
import ghidra.program.model.listing.Data;
import ghidra.program.model.listing.DataIterator;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.listing.InstructionIterator;
import ghidra.program.model.mem.MemoryBlock;
import ghidra.program.model.mem.MemoryBlockSourceInfo;
import ghidra.program.model.symbol.Symbol;
import ghidra.program.model.symbol.SymbolIterator;
import ghidra.program.model.symbol.Reference;
import ghidra.program.model.symbol.ReferenceManager;

public class ROREExport extends HeadlessScript {
    private static final int MAX_FUNCTIONS = 10000;
    private static final int MAX_STRINGS = 10000;
    private static final int MAX_SYMBOLS = 10000;
    private static final int MAX_STRING_CHARS = 4096;
    private static final int MAX_DECOMPILE_CHARS = 10_000_000;
    private static final int MAX_INSTRUCTIONS = 10000;
    private static final int MAX_REFERENCES = 10000;

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (currentProgram == null || args.length != 2) {
            throw new IllegalArgumentException("ROREExport requires output JSON path and address-or-none");
        }
        File output = new File(args[0]);
        File parent = output.getParentFile();
        if (parent == null || !parent.isDirectory() || output.exists()) {
            throw new IllegalArgumentException("RORE output must be a new file in an existing directory");
        }

        JsonObject root = new JsonObject();
        root.addProperty("schema_version", 1);
        root.addProperty("provider", "ghidra-headless");
        root.addProperty("auto_analysis_timed_out", analysisTimeoutOccurred());
        JsonObject program = new JsonObject();
        program.addProperty("name", currentProgram.getName());
        program.addProperty("executable_path", currentProgram.getExecutablePath());
        program.addProperty("executable_format", currentProgram.getExecutableFormat());
        program.addProperty("language_id", currentProgram.getLanguageID().getIdAsString());
        program.addProperty("compiler_spec_id", currentProgram.getCompilerSpec().getCompilerSpecID().getIdAsString());
        program.addProperty("image_base", currentProgram.getImageBase().toString());
        program.addProperty("executable_md5", currentProgram.getExecutableMD5());
        root.add("program", program);

        JsonArray blocks = new JsonArray();
        for (MemoryBlock block : currentProgram.getMemory().getBlocks()) {
            monitor.checkCancelled();
            JsonObject item = new JsonObject();
            item.addProperty("name", block.getName());
            item.addProperty("start", block.getStart().toString());
            item.addProperty("end", block.getEnd().toString());
            item.addProperty("initialized", block.isInitialized());
            item.addProperty("read", block.isRead());
            item.addProperty("write", block.isWrite());
            item.addProperty("execute", block.isExecute());
            JsonArray sources = new JsonArray();
            for (MemoryBlockSourceInfo source : block.getSourceInfos()) {
                JsonObject sourceItem = new JsonObject();
                sourceItem.addProperty("start", source.getMinAddress().toString());
                sourceItem.addProperty("end", source.getMaxAddress().toString());
                sourceItem.addProperty("description", source.getDescription());
                sourceItem.addProperty("file_bytes_offset", source.getFileBytesOffset());
                sourceItem.addProperty("file_backed", source.getFileBytes().isPresent());
                sources.add(sourceItem);
            }
            item.add("sources", sources);
            blocks.add(item);
        }
        root.add("memory_blocks", blocks);

        JsonObject functions = new JsonObject();
        JsonArray functionItems = new JsonArray();
        int managerReportedFunctions = currentProgram.getFunctionManager().getFunctionCount();
        int enumeratedFunctions = 0;
        FunctionIterator functionIterator = currentProgram.getFunctionManager().getFunctions(true);
        while (functionIterator.hasNext()) {
            monitor.checkCancelled();
            Function function = functionIterator.next();
            enumeratedFunctions++;
            if (functionItems.size() >= MAX_FUNCTIONS) {
                continue;
            }
            JsonObject item = new JsonObject();
            item.addProperty("name", function.getName());
            item.addProperty("entry", function.getEntryPoint().toString());
            item.addProperty("body_addresses", function.getBody().getNumAddresses());
            item.addProperty("external", function.isExternal());
            item.addProperty("thunk", function.isThunk());
            item.addProperty("prototype", function.getPrototypeString(true, true));
            functionItems.add(item);
        }
        functions.addProperty("total", enumeratedFunctions);
        functions.addProperty("manager_reported_total", managerReportedFunctions);
        functions.addProperty("emitted", functionItems.size());
        functions.addProperty("complete", enumeratedFunctions == functionItems.size());
        functions.add("items", functionItems);
        root.add("functions", functions);

        JsonObject strings = new JsonObject();
        JsonArray stringItems = new JsonArray();
        int stringTotal = 0;
        DataIterator dataIterator = currentProgram.getListing().getDefinedData(true);
        while (dataIterator.hasNext()) {
            monitor.checkCancelled();
            Data data = dataIterator.next();
            if (!data.hasStringValue()) {
                continue;
            }
            stringTotal++;
            if (stringItems.size() >= MAX_STRINGS) {
                continue;
            }
            Object value = data.getValue();
            String text = value == null ? "" : value.toString();
            JsonObject item = new JsonObject();
            item.addProperty("address", data.getAddress().toString());
            item.addProperty("length_bytes", data.getLength());
            item.addProperty("value_length_chars", text.length());
            item.addProperty("value_complete", text.length() <= MAX_STRING_CHARS);
            item.addProperty("value", text.substring(0, Math.min(text.length(), MAX_STRING_CHARS)));
            stringItems.add(item);
        }
        strings.addProperty("total", stringTotal);
        strings.addProperty("emitted", stringItems.size());
        strings.addProperty("complete", stringTotal == stringItems.size());
        strings.add("items", stringItems);
        root.add("strings", strings);

        JsonObject externals = new JsonObject();
        JsonArray externalItems = new JsonArray();
        int externalTotal = 0;
        SymbolIterator externalIterator = currentProgram.getSymbolTable().getExternalSymbols();
        while (externalIterator.hasNext()) {
            monitor.checkCancelled();
            Symbol symbol = externalIterator.next();
            externalTotal++;
            if (externalItems.size() >= MAX_SYMBOLS) {
                continue;
            }
            JsonObject item = new JsonObject();
            item.addProperty("name", symbol.getName(true));
            item.addProperty("address", symbol.getAddress().toString());
            item.addProperty("source", symbol.getSource().toString());
            externalItems.add(item);
        }
        externals.addProperty("total", externalTotal);
        externals.addProperty("emitted", externalItems.size());
        externals.addProperty("complete", externalTotal == externalItems.size());
        externals.add("items", externalItems);
        root.add("external_symbols", externals);

        JsonObject entryPoints = new JsonObject();
        JsonArray entryItems = new JsonArray();
        int entryTotal = 0;
        AddressIterator entryIterator = currentProgram.getSymbolTable().getExternalEntryPointIterator();
        while (entryIterator.hasNext()) {
            monitor.checkCancelled();
            Address entry = entryIterator.next();
            entryTotal++;
            if (entryItems.size() < MAX_SYMBOLS) {
                entryItems.add(entry.toString());
            }
        }
        entryPoints.addProperty("total", entryTotal);
        entryPoints.addProperty("emitted", entryItems.size());
        entryPoints.addProperty("complete", entryTotal == entryItems.size());
        entryPoints.add("items", entryItems);
        root.add("external_entry_points", entryPoints);

        if (!"none".equals(args[1])) {
            JsonObject selected = new JsonObject();
            selected.addProperty("requested_address", args[1]);
            Address address = currentProgram.getAddressFactory().getAddress(args[1]);
            Function function = address == null ? null : currentProgram.getFunctionManager().getFunctionContaining(address);
            if (function == null) {
                selected.addProperty("status", "no_function_at_address");
            } else {
                selected.addProperty("function_entry", function.getEntryPoint().toString());
                JsonObject instructionInventory = new JsonObject();
                JsonArray instructionItems = new JsonArray();
                int instructionTotal = 0;
                JsonObject referenceInventory = new JsonObject();
                JsonArray referenceItems = new JsonArray();
                int referenceTotal = 0;
                ReferenceManager referenceManager = currentProgram.getReferenceManager();
                InstructionIterator instructions = currentProgram.getListing().getInstructions(function.getBody(), true);
                while (instructions.hasNext()) {
                    monitor.checkCancelled();
                    Instruction instruction = instructions.next();
                    instructionTotal++;
                    for (Reference reference : referenceManager.getReferencesFrom(instruction.getAddress())) {
                        referenceTotal++;
                        if (referenceItems.size() < MAX_REFERENCES) {
                            JsonObject item = new JsonObject();
                            item.addProperty("from", reference.getFromAddress().toString());
                            item.addProperty("from_space", reference.getFromAddress().getAddressSpace().getName());
                            item.addProperty("to", reference.getToAddress().toString());
                            item.addProperty("to_space", reference.getToAddress().getAddressSpace().getName());
                            item.addProperty("type", reference.getReferenceType().getName());
                            item.addProperty("source", reference.getSource().toString());
                            item.addProperty("operand_index", reference.getOperandIndex());
                            item.addProperty("external", reference.isExternalReference());
                            item.addProperty("memory", reference.isMemoryReference());
                            item.addProperty("stack", reference.isStackReference());
                            item.addProperty("register", reference.isRegisterReference());
                            item.addProperty("flow", reference.getReferenceType().isFlow());
                            item.addProperty("read", reference.getReferenceType().isRead());
                            item.addProperty("write", reference.getReferenceType().isWrite());
                            item.addProperty("indirect", reference.getReferenceType().isIndirect());
                            referenceItems.add(item);
                        }
                    }
                    if (instructionItems.size() < MAX_INSTRUCTIONS) {
                        JsonObject item = new JsonObject();
                        item.addProperty("address", instruction.getAddress().toString());
                        item.addProperty("bytes_hex", HexFormat.of().formatHex(instruction.getBytes()));
                        item.addProperty("listing", instruction.toString());
                        instructionItems.add(item);
                    }
                }
                instructionInventory.addProperty("total", instructionTotal);
                instructionInventory.addProperty("emitted", instructionItems.size());
                instructionInventory.addProperty("complete", instructionTotal == instructionItems.size());
                instructionInventory.add("items", instructionItems);
                selected.add("instructions", instructionInventory);
                referenceInventory.addProperty("total", referenceTotal);
                referenceInventory.addProperty("emitted", referenceItems.size());
                referenceInventory.addProperty("complete", referenceTotal == referenceItems.size());
                referenceInventory.add("items", referenceItems);
                selected.add("references", referenceInventory);
                JsonArray callers = new JsonArray();
                Set<Function> calling = function.getCallingFunctions(monitor);
                for (Function caller : calling) {
                    callers.add(caller.getEntryPoint().toString());
                }
                selected.add("calling_functions", callers);
                JsonArray callees = new JsonArray();
                Set<Function> called = function.getCalledFunctions(monitor);
                for (Function callee : called) {
                    callees.add(callee.getEntryPoint().toString());
                }
                selected.add("called_functions", callees);
                DecompInterface decompiler = new DecompInterface();
                try {
                    if (!decompiler.openProgram(currentProgram)) {
                        selected.addProperty("status", "decompiler_open_failed");
                    } else {
                        DecompileResults result = decompiler.decompileFunction(function, 60, monitor);
                        if (!result.decompileCompleted() || result.getDecompiledFunction() == null) {
                            selected.addProperty("status", "decompile_failed");
                            selected.addProperty("error", result.getErrorMessage());
                        } else {
                            String c = result.getDecompiledFunction().getC();
                            if (c.length() > MAX_DECOMPILE_CHARS) {
                                selected.addProperty("status", "decompile_output_over_limit");
                                selected.addProperty("character_count", c.length());
                            } else {
                                File decompile = new File(parent, "decompile.c");
                                Files.writeString(decompile.toPath(), c, StandardCharsets.UTF_8);
                                selected.addProperty("status", "decompiled");
                                selected.addProperty("output_file", decompile.getName());
                                selected.addProperty("character_count", c.length());
                            }
                        }
                    }
                } finally {
                    decompiler.dispose();
                }
            }
            root.add("selected_function", selected);
        }

        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        Files.writeString(output.toPath(), gson.toJson(root), StandardCharsets.UTF_8);
        println("RORE_EXPORT_COMPLETE " + output.getAbsolutePath());
    }
}
