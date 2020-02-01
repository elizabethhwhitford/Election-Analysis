# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Analysis/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# county variables, lists, and dictionaries
counties = []
county_votes = {}
largest_county_votes = 0
largestpercent_county = 0
largest_county = ""
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0   
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
           
        # Get the county name from each row and add to counties list.    
        county_name = row[1]
        if county_name not in counties:
            counties.append(county_name)
            # each county's votes start at zero. 
            county_votes[county_name] = 0
        # add 1 for every row that has that county's name. 
        county_votes[county_name] += 1
print(county_votes)

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
    #Create header line for output
    county_results = (
        f"\nCounty Votes:\n")
    print(county_results)
    txt_file.write(county_results)
    
    #Find the percentage of votes per county
    for county_name in county_votes:
        cvotes = county_votes[county_name]
        county_percentage = float(cvotes) / float(total_votes) * 100
        # add fianl county results to text file
        final_county_results = (f"{county_name}: {county_percentage:.1f}% ({cvotes:,})\n")
        txt_file.write(final_county_results)
        #find the largest number of votes by county
        if cvotes > largest_county_votes and (county_percentage > largestpercent_county):
            largest_county_votes = cvotes
            largest_county = county_name
            largestpercent_county = county_percentage
        
# Print the county results to the terminal.
    largestcounty_results = (
        f"--------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"__________________________\n")
    print(largestcounty_results)
    txt_file.write(largestcounty_results)
         
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their voter count, and percentage to the
        # terminal.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    # print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)