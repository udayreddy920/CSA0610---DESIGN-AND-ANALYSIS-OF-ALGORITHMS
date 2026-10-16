import math
import csv

RATE = 10**8
SIZES = [1_000, 10_000, 100_000, 1_000_000]

def m1(n):
    return n * (n - 1) // 2

def m2(n):
    if n <= 1:
        return 0
    return 2 ** math.ceil(math.log2(n)) - 1

def s2(n):
    return math.ceil(math.log2(n)) + 1 if n > 1 else 1

def m4_current(n):
    # Illustrative power-of-two scale formula for T(n)=4T(n/2)+n, T(1)=1
    return 2 * n * n - n

def m4_redesign(n):
    # Illustrative formula for T(n)=2T(n/2)+n
    return n * math.ceil(math.log2(n)) + n if n > 1 else 1

def m5(n):
    # Scale estimate for T(n)=2T(n/2)+n log2(n)
    return round(n * math.log2(n) ** 2) if n > 1 else 1

def report_cost(n):
    return round(3 * n * n + 10 * n * math.log2(n) + 50)

def fmt(x):
    return f"{x:,}"

def main():
    print("SHOPSPHERE CO1 SCALABILITY AUDIT")
    print("Assumed rate:", fmt(RATE), "basic operations/second")
    print("\nM2 verification at n=1,024:", fmt(m2(1024)), "audits")
    print("Expected sum: 1 + 2 + 4 + ... + 512 = 1,023")
    print("\nScalability estimates")
    for n in SIZES:
        print("\nn =", fmt(n))
        print("M1 comparisons:", fmt(m1(n)))
        print("M2 audits:", fmt(m2(n)))
        print("S2 comparisons (estimate):", fmt(s2(n)))
        print("M4 current (illustrative):", fmt(m4_current(n)))
        print("M4 redesign (illustrative):", fmt(m4_redesign(n)))
        print("M5 recurrence (scale estimate):", fmt(m5(n)))
        print("Report f(n):", fmt(report_cost(n)))
    n = 1_000_000
    print("\nEstimated seconds at n=1,000,000")
    for label, ops in [
        ("M1", m1(n)), ("M2", m2(n)), ("S2", s2(n)),
        ("M4 current", m4_current(n)), ("M4 redesign", m4_redesign(n)),
        ("M5 recurrence", m5(n)), ("Report generator f(n)", report_cost(n))
    ]:
        print(label + ":", fmt(ops), "operations;", f"{ops/RATE:.6f}", "seconds")

    with open("Scalability_Results.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["n","M1_comparisons","M2_audits","S2_comparison_estimate",
                    "M4_current_illustrative","M4_redesign_illustrative",
                    "M5_recurrence_scale_estimate","report_generator_operations"])
        for n in SIZES:
            w.writerow([n,m1(n),m2(n),s2(n),m4_current(n),m4_redesign(n),m5(n),report_cost(n)])
    print("\nSaved Scalability_Results.csv")

if __name__ == "__main__":
    main()
