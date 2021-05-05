import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago", "new york city", "washington","all"]
    city = input("which city's data will you like to view? Chicago, New York City, Washington or all\n")
    while city.lower().strip() not in cities:
        city = input("wrong input! Please type in any of the following cities Chicago, New York City, Washington\n")

    # get user input for month (all, january, february, ... , june)

    months = ["all", "january", "february","march","april","may","june"]
    month = input("which month's data do you want to view? January, February,March,April,May,June or All\n")
    while month.lower().strip() not in months:
        month = input("wrong input!Please type in any of the following January, February,March,April,May,June or All\n")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days =  ["all", "monday", "tuesday", "wednesday","thursday","friday","saturday", "sunday"]
    day = input("which day of the week will you like to view? Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday or All\n")
    while day.lower().strip() not in days:
        day = input(
            "wrong input! Please type in any of the following Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday or All\n")




    print('-'*40)
    return city, month, day

def cities_summary(month, day):
    """
    Loads data for the all cities and filters by month and day if applicable.

    Args:
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing cities data filtered by month and day
    """
    df = pd.DataFrame()
    for city in CITY_DATA:
        df1 = pd.read_csv(CITY_DATA[city])
        pd.concat([df, df1], sort=False, ignore_index=True).fillna(0)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df["month"].value_counts(sort=True).index
    print('Most Common Month:',common_month[0])

    # display the most common day of week

    common_day = df["day_of_week"].value_counts(sort=True).index[0]
    print('Most Common Day Of The Week',common_day)

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took {} seconds.".format(time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df["Start Station"].value_counts(sort=True).index[0]
    print('Most Commonly Used End Station', common_start_station)
    # display most commonly used end station
    common_end_station = df["End Station"].value_counts(sort=True).index[0]
    print('Most Commonly Used End Station', common_end_station)
    # display most frequent combination of start station and end station trip
    common_start_end_station = df[["Start Station","End Station"]].value_counts(sort=True).index[0]
    print('Most Commonly Used Start And End Station', common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total Travel Time Is:", total_travel_time)

    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("The Mean Travel Time Is:",mean_travel_time)

    print("\nThis took {} seconds.".format(time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users. based on gender and birth date"""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    print(user_types)
    print("\n")

    if "Gender" in df.columns:
        # Display counts of gender
        gender = df['Gender'].value_counts()

        print(gender)
        print("\n")

        # Display earliest, most recent, and most common year of birth
        earliest = df["Birth Year"].iloc[-1]
        most_recent = df["Birth Year"].iloc[0]
        most_common = df["Birth Year"].mode()[0]

        print("Earliest Year Of Birth:",earliest)
        print("Most Recent Year Of Birth:", most_recent)
        print("Most Common Year Of Birth:", most_common)


    print("\nThis took {} seconds.".format(time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        if city == "all":
            df = cities_summary(month, day)
        else:
            df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

