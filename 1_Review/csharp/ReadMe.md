# C# Review Examples

This folder contains both regular C# source files (`.cs`) and C# script files (`.csx`). The examples are designed to run without creating a `.csproj` project.

## Prerequisite

Install the .NET SDK 10 or later. Verify it is available:

```bash
dotnet --version
```

## Run a regular C# file

From this folder, run a file directly:

```bash
dotnet run 1_basic_concepts.cs
```

Or run it from any directory by providing its path:

```bash
dotnet run path\to\1_basic_concepts.cs
```

The first run may download the required .NET runtime components; later runs reuse the local cache.

## C# script files (`.csx`)

Some examples use `.csx` script files, which are meant for quick scripting and experimentation rather than creating a full project. They often use `#load` to import other script files or helper modules.

Example from `4_custom_modules_and_classes.csx`:

```csharp
#load "Models/Cat.csx"
#load "Models/Dog.csx"
#load "Models/Person.csx"

var p1 = new Person("Alice", 30);
p1.Greet();
```

This pattern loads reusable script definitions before using them in the main script.

## Run a `.csx` script

A common tool for `.csx` files is `dotnet-script`:

```bash
dotnet tool install --global dotnet-script
```

Then run a script like this:

```bash
dotnet script 4_custom_modules_and_classes.csx
```

If you prefer C# Interactive, you can also run scripts with `csi` when it is installed on your machine.

## When to use `.cs` vs `.csx`

- `.cs`: best for regular class-based programs and project files.
- `.csx`: best for scripts, demos, temporary code, and modular snippets that are loaded together.

The lessons in this folder use both styles so you can compare the same concepts in a normal program and in a script-based workflow.