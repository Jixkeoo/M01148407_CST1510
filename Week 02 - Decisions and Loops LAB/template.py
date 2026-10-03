"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
label = ""
nb_over = 0

while True:

    # ==================================================================== INPUT
    # 1. Ask for your three values.
    #
    #    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
    #    - the second is a NUMBER (use float(), not int())
    #    - the third  is a NUMBER (use float(), not int())

    label = input("Enter a source IP : ")
    if label == "quit":
        break
    value = int(input("Enter number of failed login attempt : "))
    limit = int(input("Enter number of total attempts possible : "))


    # ================================================================== PROCESS
    # 2. Work out the difference and the percentage.       [Typical and above]

    difference = limit - value
    percent = value / limit * 100
    # 3. Decide a status and store it in a variable called status.
    #
    #    Threshold : if / else        -> "OVER LIMIT" or "OK"
    #    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
    #                                     "WARNING" (90% or more), otherwise "OK"

    if percent < 90:
        status = "OK"
    elif percent < 100:
        status = "WARNING"
    else:
        status = "OVER LIMIT"
        nb_over += 1


    # =================================================================== OUTPUT
    # 4. Print the report.
    #
    #    Threshold : the three values you were given, plus status, inside a border
    #    Typical   : add difference and percent, 2 decimal places, right-aligned
    #    Excellent : wrap sections 1-4 in a loop so you can check as many records
    #                as you like in one run - type "quit" as the label to stop.
    #                Keep count of how many came back OVER LIMIT and print that
    #                once, after the loop ends.

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"  Failed login attempts   : {value:11.2f}")
    print(f"  Total attempts possible : {limit:11.2f}")
    print(f"  Remaining attempts      : {difference:11.2f}")
    print(f"  Failed login percent    : {percent:11.2f} %")
    print(f"  Status                  : {status:>11}")

    print("=" * 34)

print(f"Number of over limit : {nb_over}")

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
