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

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

Source_IP = input("Enter a source IP : ")
Failed_login = int(input("Enter number of failed login attempt : "))
Total_login = int(input("Enter number of total attempts possible : "))


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

Remaining_attempts = Total_login - Failed_login
Percent_failed = Failed_login / Total_login * 100
#It can be helpful for getting a simpler idea of the remaining percentage of attempts.
Percent_remaining = 100 - Percent_failed



# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {Source_IP}")
print("=" * 34)

print(f"  Failed login attempts   : {Failed_login:+11.2f}")
print(f"  Total attempts possible : {Total_login:+11.2f}")
print(f"  Remaining attempts      : {Remaining_attempts:+11.2f}")
print(f"  Failed login percent    : {Percent_failed:+11.2f} %")
print(f"  Remaining login percent : {Percent_remaining:+11.2f} %")

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
