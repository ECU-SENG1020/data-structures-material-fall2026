
static void AssertEqual<T>(T expected, T actual, string label)
{
    if (!EqualityComparer<T>.Default.Equals(expected, actual))
    {
        throw new Exception($"{label} failed: expected {expected}, got {actual}");
    }
}

static void AssertTrue(bool condition, string label)
{
    if (!condition)
    {
        throw new Exception($"{label} failed");
    }
}

static void TestAppend()
{
    var list = new DsList<string>();
    list.Append("a");
    list.Append("b");
    list.Append("c");
    AssertEqual(3, list.Count, "Append count");
}

static void TestGetItem()
{
    var list = new DsList<string>();
    list.Append("a");
    list.Append("b");
    list.Append("c");
    AssertEqual("b", list[1], "Get item");
}

static void TestSetItem()
{
    var list = new DsList<string>();
    list.Append("a");
    list.Append("b");
    list.Append("c");
    list[1] = "d";
    AssertEqual("d", list[1], "Set item");
}

static void TestIterate()
{
    var list = new DsList<string>();
    list.Append("a");
    list.Append("b");
    var count = 0;
    foreach (var item in list)
    {
        count++;
    }
    AssertEqual(2, count, "Iteration count");
}

static void TestAdd()
{
    var left = new DsList<string>();
    left.Append("e");
    left.Append("b");

    var right = new DsList<string>();
    right.Append("f");
    right.Append("f");

    var result = left + right;
    AssertEqual(4, result.Count, "Add count");
}

static void TestContainsTrue()
{
    var list = new DsList<string>();
    list.Append("e");
    list.Append("b");
    list.Append("f");
    list.Append("f");
    AssertTrue(list.Contains("b"), "Contains true");
}

static void TestContainsFalse()
{
    var list = new DsList<string>();
    list.Append("e");
    list.Append("b");
    list.Append("f");
    list.Append("f");
    AssertTrue(!list.Contains("z"), "Contains false");
}

static void TestClear()
{
    var list = new DsList<string>();
    list.Append("e");
    list.Append("b");
    list.Append("f");
    list.Append("f");
    list.Clear();
    AssertEqual(0, list.Count, "Clear count");
}

static void Main()
{
    TestAppend();
    TestGetItem();
    TestSetItem();
    TestIterate();
    TestAdd();
    TestContainsTrue();
    TestContainsFalse();
    TestClear();
    Console.WriteLine("All list tests passed.");
}

Main();
