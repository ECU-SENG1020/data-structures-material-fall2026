# C# Review Examples

These examples are standalone C# files and do not require a `.csproj` project.

## Prerequisite

Install the .NET SDK 10 or later. Verify it is available:

```powershell
dotnet --version
```

## Run an example

From this folder, run a file directly:

```powershell
dotnet run 1_basic_concepts.cs
```

Or run it from any directory by providing its path:

```powershell
dotnet run path\to\1_basic_concepts.cs
```

The first run may download the required .NET runtime components; later runs reuse the local cache.