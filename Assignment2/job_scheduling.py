"""
Assignment No. 2
Title: Implement Greedy Search Algorithm

Application: Job Scheduling Problem

Each job has:
    - Job ID
    - Deadline
    - Profit

The objective is to schedule jobs so that the total profit is maximum.

Greedy Choice:
    Select jobs in decreasing order of profit and place each job
    in the latest available slot before its deadline.

Time Complexity:
    O(n^2) using the simple slot-search implementation.

Space Complexity:
    O(n)
"""


def job_scheduling(jobs):
    """
    Schedule jobs to maximize total profit.

    Parameters:
        jobs (list): List of tuples:
                     (job_id, deadline, profit)

    Returns:
        tuple:
            scheduled_jobs: List of scheduled job IDs
            total_profit: Maximum profit obtained
    """

    if not jobs:
        return [], 0

    # Validate jobs.
    for job in jobs:
        if len(job) != 3:
            raise ValueError(
                "Each job must contain (job_id, deadline, profit)."
            )

        job_id, deadline, profit = job

        if deadline <= 0:
            raise ValueError(
                f"Invalid deadline for job {job_id}: {deadline}"
            )

    # Greedy choice:
    # Process jobs from highest profit to lowest profit.
    sorted_jobs = sorted(jobs, key=lambda job: job[2], reverse=True)

    # Maximum useful number of slots is the number of jobs.
    max_deadline = min(
        max(job[1] for job in sorted_jobs),
        len(sorted_jobs)
    )

    slots = [None] * max_deadline

    total_profit = 0
    scheduled_jobs = []

    for job_id, deadline, profit in sorted_jobs:

        # Start from the latest possible slot.
        latest_slot = min(deadline, max_deadline)

        for slot in range(latest_slot - 1, -1, -1):

            if slots[slot] is None:
                slots[slot] = job_id
                total_profit += profit
                scheduled_jobs.append(job_id)
                break

    # Return jobs in chronological slot order.
    scheduled_jobs = [
        job_id for job_id in slots if job_id is not None
    ]

    return scheduled_jobs, total_profit


def main():
    """Demonstrate Job Scheduling."""
    jobs = [
        ("J1", 2, 100),
        ("J2", 1, 19),
        ("J3", 2, 27),
        ("J4", 1, 25),
        ("J5", 3, 15)
    ]

    scheduled_jobs, total_profit = job_scheduling(jobs)

    print("=" * 50)
    print("JOB SCHEDULING")
    print("=" * 50)

    print("Jobs:")
    for job in jobs:
        print(f"  {job[0]} -> Deadline: {job[1]}, Profit: {job[2]}")

    print("\nScheduled Jobs:", scheduled_jobs)
    print("Total Profit:", total_profit)


if __name__ == "__main__":
    main()
