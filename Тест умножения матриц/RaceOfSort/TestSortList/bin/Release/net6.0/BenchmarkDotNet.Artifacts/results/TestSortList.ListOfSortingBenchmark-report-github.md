``` ini

BenchmarkDotNet=v0.13.1, OS=Windows 10.0.19044.1826 (21H2)
Intel Xeon CPU X3440 2.53GHz, 1 CPU, 8 logical and 4 physical cores
.NET SDK=6.0.101
  [Host]     : .NET 6.0.1 (6.0.121.56705), X64 RyuJIT  [AttachedDebugger]
  DefaultJob : .NET 6.0.1 (6.0.121.56705), X64 RyuJIT


```
|                Method |    Mean |    Error |   StdDev | Rank | Allocated |
|---------------------- |--------:|---------:|---------:|-----:|----------:|
|         TestSerialMul | 9.872 s | 0.1569 s | 0.1611 s |    2 |      4 KB |
| TestParallelMulThread | 1.820 s | 0.0279 s | 0.0248 s |    1 |      3 KB |
|   TestParallelMulTask | 1.796 s | 0.0044 s | 0.0035 s |    1 |      3 KB |
