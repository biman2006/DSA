def happy_number(n):
    def sum_digit(num):
        total=0
        while num>0:
            digit=num%10
            total+=digit**2
            num//=10
        return total

    slow=n
    fast=n

    while slow!=1:
        slow=sum_digit(slow)
        fast=sum_digit(sum_digit(fast))

        if slow==fast and slow!=1:
            return False
    return True 


if __name__=="__main__":
    print(happy_number(2))



"""

FULL EXPLANATION:



============================================================
                HAPPY NUMBER
        Using Fast & Slow Pointer
============================================================


1. WHAT IS A HAPPY NUMBER?
--------------------------

A number is called a Happy Number if repeatedly:

    1. Take each digit of the number.
    2. Square each digit.
    3. Add all the squared digits.
    4. Repeat the same process.

If eventually the result becomes 1, the number is Happy.

If the process enters a cycle and never reaches 1,
the number is NOT Happy.


============================================================
2. BASIC EXAMPLE
============================================================

Take n = 19

Step 1:

    19

    1² + 9²
    = 1 + 81
    = 82


Step 2:

    82

    8² + 2²
    = 64 + 4
    = 68


Step 3:

    68

    6² + 8²
    = 36 + 64
    = 100


Step 4:

    100

    1² + 0² + 0²
    = 1


We reached 1.

Therefore:

    19 is a HAPPY NUMBER.


============================================================
3. WHY DO WE NEED FAST AND SLOW POINTER?
============================================================

The problem is that an unhappy number does not stop.

Instead, it enters a cycle.

For example, take n = 2:


    2
    ↓
    4
    ↓
    16
    ↓
    37
    ↓
    58
    ↓
    89
    ↓
    145
    ↓
    42
    ↓
    20
    ↓
    4
    ↓
    16
    ↓
    ...


Notice:

    4 → 16 → 37 → 58 → ... → 20 → 4

The sequence is repeating.

Therefore, it will NEVER reach 1.

We need some way to detect this cycle.

This is where Fast and Slow Pointer is useful.


============================================================
4. WHAT ARE SLOW AND FAST?
============================================================

We consider every number in the sequence as a node.

For example:

    19 → 82 → 68 → 100 → 1

Slow moves one step at a time.

Fast moves two steps at a time.


For example:

    Slow:
    19 → 82 → 68 → 100 → 1

    Fast:
    19 → 68 → 1


This is the same idea used in Linked List Cycle Detection.


============================================================
5. WHAT DOES ONE STEP MEAN?
============================================================

One step means:

    Take the current number
    ↓
    Calculate the sum of squares of its digits
    ↓
    Get the next number


Example:

    19 → 82

because:

    1² + 9² = 82


Therefore:

    One step from 19 = 82


Two steps from 19:

    19 → 82 → 68

So:

    Two steps from 19 = 68


============================================================
6. DRY RUN FOR 19
============================================================

Initial:

    slow = 19
    fast = 19


------------------------------------------------------------
ITERATION 1
------------------------------------------------------------

Slow moves ONE step:

    19 → 82

Therefore:

    slow = 82


Fast moves TWO steps:

    19 → 82 → 68

Therefore:

    fast = 68


Now compare:

    slow = 82
    fast = 68

They are NOT equal.

Continue.


------------------------------------------------------------
ITERATION 2
------------------------------------------------------------

Current:

    slow = 82
    fast = 68


Slow moves ONE step:

    82 → 68

Therefore:

    slow = 68


Fast moves TWO steps:

    68 → 100 → 1

Therefore:

    fast = 1


Compare:

    slow = 68
    fast = 1

They are NOT equal.

Continue.


------------------------------------------------------------
ITERATION 3
------------------------------------------------------------

Current:

    slow = 68
    fast = 1


Slow moves ONE step:

    68 → 100

Therefore:

    slow = 100


Fast moves TWO steps:

    1 → 1 → 1

Therefore:

    fast = 1


Compare:

    slow = 100
    fast = 1

They are NOT equal.

Continue.


------------------------------------------------------------
ITERATION 4
------------------------------------------------------------

Current:

    slow = 100
    fast = 1


Slow moves ONE step:

    100 → 1

Therefore:

    slow = 1


Fast moves TWO steps:

    1 → 1 → 1

Therefore:

    fast = 1


Now:

    slow = 1
    fast = 1


They meet.

And they meet at:

    1


Therefore:

    19 is HAPPY.


Answer:

    TRUE


============================================================
7. WHY DOES SLOW == FAST MATTER?
============================================================

When slow and fast become equal, it means they are at the
same position in the sequence.

Because fast is moving faster than slow, if the sequence
contains a cycle, fast will eventually catch slow.

This is exactly the same idea as a circular running track.

Imagine:

    Slow  → runs slowly
    Fast  → runs quickly

If the track is circular, the fast runner will eventually
catch the slow runner.

Therefore:

    slow == fast

means:

    A cycle has been detected.


============================================================
8. BUT THERE IS AN IMPORTANT EXCEPTION
============================================================

For a Happy Number, the sequence ends at 1.

But after reaching 1:

    1 → 1 → 1 → 1 → ...


So technically, 1 is also a cycle.

Therefore, when slow and fast meet, we MUST check where
they met.

There are two possibilities.


CASE 1:

    slow == fast == 1

This means:

    The sequence reached 1.

Therefore:

    HAPPY → TRUE


CASE 2:

    slow == fast != 1

This means:

    The sequence is stuck in a cycle that does not contain 1.

Therefore:

    NOT HAPPY → FALSE


============================================================
9. DRY RUN FOR 2
============================================================

Initial:

    slow = 2
    fast = 2


------------------------------------------------------------
ITERATION 1
------------------------------------------------------------

Slow:

    2 → 4

    slow = 4


Fast:

    2 → 4 → 16

    fast = 16


Compare:

    4 != 16

Continue.


------------------------------------------------------------
ITERATION 2
------------------------------------------------------------

Slow:

    4 → 16

    slow = 16


Fast:

    16 → 37 → 58

    fast = 58


Compare:

    16 != 58

Continue.


------------------------------------------------------------
ITERATION 3
------------------------------------------------------------

Slow:

    16 → 37

    slow = 37


Fast:

    58 → 89 → 145

    fast = 145


Compare:

    37 != 145

Continue.


Eventually, both pointers continue moving through the cycle.


The sequence is:

    2 → 4 → 16 → 37 → 58 → 89 → 145
      → 42 → 20 → 4 → 16 → ...


Eventually:

    slow = 4
    fast = 4


They meet.

But:

    slow = 4

NOT:

    slow = 1


Therefore:

    NOT HAPPY → FALSE


============================================================
10. COMPLETE LOGIC
============================================================

Start with:

    slow = n
    fast = n


Then repeat:

    Slow moves ONE step.

    Fast moves TWO steps.


Now ask:

    Did slow reach 1?

If YES:

    The number is Happy.


If NO:

    Check whether slow == fast.


If:

    slow == fast

then a cycle has been detected.


Now check where they met:

    If they met at 1:
        TRUE

    If they met somewhere else:
        FALSE


============================================================
11. THE MOST IMPORTANT CONCEPT
============================================================

Remember this:

    SLOW = ONE STEP

    FAST = TWO STEPS


And:

    slow == fast
        ↓
    Cycle detected


But:

    slow == fast == 1
        ↓
    Happy Number


Whereas:

    slow == fast != 1
        ↓
    Unhappy Number


============================================================
12. CONNECTION WITH LINKED LIST
============================================================

You already learned Fast and Slow Pointer for
Linked List Cycle Detection.

In a linked list:

    slow = slow.next

    fast = fast.next.next


For Happy Number, there is no actual linked list.

Instead, the "next node" is:

    Sum of squares of digits


So conceptually:

    Linked List:

        slow → next
        fast → next → next


    Happy Number:

        slow → sum of squares
        fast → sum of squares → sum of squares


The concept is EXACTLY the same:

    FAST catches SLOW when there is a cycle.


============================================================
13. FINAL SUMMARY
============================================================

Happy Number problem:

    Step 1:
        Calculate sum of squares of digits.

    Step 2:
        Use Slow and Fast pointers.

    Step 3:
        Slow moves one step.

    Step 4:
        Fast moves two steps.

    Step 5:
        If they meet at 1:
            TRUE

    Step 6:
        If they meet somewhere other than 1:
            FALSE


For 19:

    19 → 82 → 68 → 100 → 1

    Result = TRUE


For 2:

    2 → 4 → 16 → 37 → ... → 20 → 4 → ...

    Result = FALSE


KEY IDEA:

    slow == fast
         ↓
    Cycle detected
         ↓
    Did they meet at 1?
       /       \
     YES       NO
      ↓         ↓
    TRUE      FALSE


============================================================





"""