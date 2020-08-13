import time
import pandas as pd
import numpy as np

city_data = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_data = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
day_data = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nWelcome! I\'ve assembled bikeshare data from a few cities in the United States. Let\'s closely analyze the data based on your specific inputs. ')

    # This gets the user's input for the following cities: chicago, new york city, washington. It also provides a response when there is a invalid input.

    city = ''

    while city not in city_data:
        city = input('\nPlease input one of the following city names: chicago, new york city or washington \n').lower()
        if city in city_data:
            print('\nThank you. I have registered your selection of:',city.lower())
            break
        else:
            print('\nThat wasn\'t one of the following city names: chicago, new york, or washington. Please try again.')

    # This gets the user's input for the following options: all, january, february, march, april, may, or june. It also provides a response when there is an invalid input.

    month = ''

    while month not in month_data:
        month = input('\nPlease input one of the following options: all, january, february, march, april, may, or june.\n').lower()
        if month in month_data:
            print('\nThank you. I have registered your selection of:', month.lower())
            break
        else:
            print('\nThat wasn\'t one of the following options: all, january, february, march, april, may, or june. Please try again.')

    # This gets the user input for day of week (all, monday, tuesday, ... sunday)

    day = ''

    while day not in day_data:
        day = input('\nPlease input one of the following options: all, monday, tuesday, wednesday, thursday, friday, saturday, sunday.\n').lower()
        if day in day_data:
            print('\nThank you. I have registered your selection of:', day.lower())
            break
        else:
            print('\nThat wasn\'t one of the following options: all, monday, tuesday, wednesday, thursday, friday, saturday, sunday. Please try again.')
            break
    print('-'*55)
    return city, month, day


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

    df = pd.read_csv(city_data[city])

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nI\'ve combined all of your specific inputs and will return calculated outputs below. Please enjoy this haiku while you wait:\n\nDelightful distance,\n\ncontrasting great colours,\n\nirreplaceable thoughts.\n\n-------------------------\n')
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # This displays the most common month
    df['month'] = df['Start Time'].dt.month
    month_comm = df['month'].mode()[0]
    print("The most usage occurs during the month of {}.\n".format(month_comm))

    # This displays the most common day of week
    df['day'] = df['Start Time'].dt.day
    day_comm = df['day'].mode()[0]
    print("The most common day of travel is {}.\n".format(day_comm))

    # This displays the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    hour_comm = df['hour'].mode()[0]
    return print("The most common hour of travel is at {}.\n".format(hour_comm))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # This displays the most commonly used start station
    start_comm = df['Start Station'].mode()[0]



    # This displays most commonly used end station
    end_comm = df['End Station'].mode()[0]

    print("The most commonly used starting and ending stations are {} and {}.\n".format(start_comm, end_comm))


    # This displays most frequent combination of start station and end station trip
    freq_combinat = df.groupby(['Start Station','End Station']).size().nlargest(1)

    print("The most frequent start station to end station combination is {}.".format(freq_combinat))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*38)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # This displays total travel time

    total = df['Trip Duration'].sum()


    # This displays mean travel time
    avg = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*38)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # This displays counts of user types
    user_types = df['User Type'].value_counts()
    print('The user types are: ', user_types)

    # This displays counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print("The count of user gender from the given fitered data is: \n" + str(gender_count))
    except:
        print("Sorry. No data available!")
        print('Washington does not have gender information')


    # This displays earliest, most recent, and most common year of birth
    try:
        earliest_birth = int(df['Birth Year'].min())
        latest_birth = int(df['Birth Year'].max())
        common_birth = int(df['Birth Year'].mode())
        print('Earliest birth year from the given fitered data is: {}\n'.format(earliest_birth))
        print('Most recent birth year from the given fitered data is: {}\n'.format(latest_birth))
        print('Most common birth year from the given fitered data is: {}\n'.format(common_birth))
    except:
        print("Sorry. No data available!")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*38)

def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to see the next rows of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
