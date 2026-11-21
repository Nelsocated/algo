import timeit
import cProfile
from collections import deque

def appendMethod(n: int):
    nums = []
    for i in range(n):
        nums.append(i)
    return nums

def insertMethod(n: int):
    nums = []
    for i in range(n):
        nums.insert(0, i)
    return nums

def appendLeftMethod(n: int):
    nums = deque()
    for i in range(n):
        nums.appendleft(i)
    return nums

print("Append (10_000): ", timeit.timeit(lambda: appendMethod(10_000), number=100))
print("Insert (10_000): ", timeit.timeit(lambda: insertMethod(10_000), number=100))
print("Append Left (10_000): ", timeit.timeit(lambda: appendLeftMethod(10_000), number=100))

print("Append (20_000): ", timeit.timeit(lambda: appendMethod(20_000), number=100))
print("Insert (20_000): ", timeit.timeit(lambda: insertMethod(20_000), number=100))
print("Append Left (20_000): ", timeit.timeit(lambda: appendLeftMethod(20_000), number=100))

print("Append (40_000): ", timeit.timeit(lambda: appendMethod(40_000), number=100))
print("Insert (40_000): ", timeit.timeit(lambda: insertMethod(40_000), number=100))
print("Append Left (40_000): ", timeit.timeit(lambda: appendLeftMethod(40_000), number=100))

print("Append (80_000): ", timeit.timeit(lambda: appendMethod(80_000), number=100))
print("Insert (80_000): ", timeit.timeit(lambda: insertMethod(80_000), number=100))
print("Append Left (80_000): ", timeit.timeit(lambda: appendLeftMethod(80_000), number=100))

def listTime(n):
    return list(range(n))

def setTime(n):
    return set(range(n))

def dictTime(n):
    return {i: i for i in range(n)}

print("List (50_000): ", timeit.timeit("-1 in c", globals={"c": listTime(50_000)}, number=10_000) * 1000)
print("Set (50_000): ", timeit.timeit("-1 in c", globals={"c": setTime(50_000)}, number=10_000) * 1000)
print("Dict (50_000): ", timeit.timeit("-1 in c", globals={"c": dictTime(50_000)}, number=10_000) * 1000)

print("List (100_000): ", timeit.timeit("-1 in c", globals={"c": listTime(100_000)}, number=10_000) * 1000)
print("Set (100_000): ", timeit.timeit("-1 in c", globals={"c": setTime(100_000)}, number=10_000) * 1000)
print("Dict (100_000): ", timeit.timeit("-1 in c", globals={"c": dictTime(100_000)}, number=10_000) * 1000)

print("List (200_000): ", timeit.timeit("-1 in c", globals={"c": listTime(200_000)}, number=10_000) * 1000)
print("Set (200_000): ", timeit.timeit("-1 in c", globals={"c": setTime(200_000)}, number=10_000) * 1000)
print("Dict (200_000): ", timeit.timeit("-1 in c", globals={"c": dictTime(200_000)}, number=10_000) * 1000)

print("List (400_000): ", timeit.timeit("-1 in c", globals={"c": listTime(400_000)}, number=10_000) * 1000)
print("Set (400_000): ", timeit.timeit("-1 in c", globals={"c": setTime(400_000)}, number=10_000) * 1000)
print("Dict (400_000): ", timeit.timeit("-1 in c", globals={"c": dictTime(400_000)}, number=10_000) * 1000)


def build_audit_report(records):
    unique_ids = []
    report = ""
    for rec_id, label in records:
        if rec_id not in unique_ids:
            unique_ids.append(rec_id)
            report += f"{rec_id}: {label}\n"
    return report

n = 30_000
records = [(i % 25_000, f"label{i}") for i in range(n)]

cProfile.run("build_audit_report(records)", sort="tottime")

def build_audit_report(records):
    seen = set()
    parts  = []
    for rec_id, label in records:
        if rec_id not in seen:
            seen.add(rec_id)
            parts.append(f"{rec_id}: {label}\n")
    return "".join(parts)

n = 30_000
records = [(i % 25_000, f"label{i}") for i in range(n)]

cProfile.run("build_audit_report(records)", sort="tottime") 

