def record_daily_yields(day):
    daily_yields = {}
    print(f"\nEntering yields for {day}.")
    while True:
        cow_id = input("Enter cow ID (3-digit code) or 'done' to finish: ")
        if cow_id.lower() == 'done':
            break
        if not cow_id.isdigit() or len(cow_id) != 3:
            print("Invalid cow ID. Please enter a 3-digit code.")
            continue
        morning_yield = float(input(f"Enter morning yield for cow {cow_id}: "))
        evening_yield = float(input(f"Enter evening yield for cow {cow_id}: "))
        daily_yields[cow_id] = [morning_yield, evening_yield]
    return daily_yields

def record_weekly_yields():
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekly_yields = {day: record_daily_yields(day) for day in days_of_the_week}
    return weekly_yields

def calculate_and_display_statistics(weekly_yields):
    """
    Calculates and displays the total weekly volume and average yield per cow.
    :param weekly_yields: A nested dictionary containing the weekly yields data.
    """
    total_volume = 0
    cow_count = len(weekly_yields)
    
    for week_data in weekly_yields.values():
        for day_yields in week_data.values():
            total_volume += sum(day_yields)
    
    average_yield_per_cow = total_volume / cow_count if cow_count else 0
    
    print("\nTotal and Average Yield Statistics")
    print(f"Total Weekly Volume: {total_volume:.0f} Litres")
    print(f"Average Yield per Cow: {average_yield_per_cow:.0f} Litres")

def identify_highest_and_low_producers(weekly_yields):
    """
    Identifies the cow with the highest total milk production over the week and
    any cows that have produced less than 12 liters on four or more days.
    """
    total_yields = {}
    low_production_days = {cow_id: 0 for cow_id in weekly_yields.keys()}  # Initialize with cow IDs
    
    for cow_id, week_data in weekly_yields.items():
        total_weekly_yield = sum([sum(day_yields) for day_yields in week_data.values()])
        total_yields[cow_id] = total_weekly_yield
        
        # Check for low production days
        for day_yields in week_data.values():
            if sum(day_yields) < 12:
                low_production_days[cow_id] += 1
    
    # Identify the highest producer
    highest_producer = max(total_yields, key=total_yields.get)
    highest_yield = total_yields[highest_producer]
    
    # Identify low producers
    low_producers = [cow_id for cow_id, days in low_production_days.items() if days >= 4]
    
    # Display the results
    print(f"\nHighest Producer: Cow {highest_producer} with {highest_yield:.1f} liters.")
    if low_producers:
        print("Low Producers (less than 12 liters on four or more days):", ', '.join(low_producers))
    else:
        print("No cows produced less than 12 liters on four or more days.")
def display_weekly_yields(weekly_yields):
    print("\nWeekly Milk Yields (Condensed View)")
    for day, yields in weekly_yields.items():
        print(f"\n{day}:")
        for cow_id, yield_data in yields.items():
            print(f"Cow {cow_id}: Morning - {yield_data[0]} liters, Evening - {yield_data[1]} liters")

def display_weekly_yields_statistics_and_producers(weekly_yields):
    display_weekly_yields(weekly_yields)
    calculate_and_display_statistics(weekly_yields)
    identify_highest_and_low_producers(weekly_yields)

# Main program execution
def main():
    weekly_yields = record_weekly_yields()
    display_weekly_yields_statistics_and_producers(weekly_yields)

if __name__ == "__main__":
    main()
