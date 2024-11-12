import pandas as pd
import os

# Define directory
directory = '/Users/manuel/Documents/GitHub/JeanPierreWeill/Data /MetaOrgarnic /GoogleSheets'

# Define correct filenames
files = {
    'fb': 'fb_post_df_clean - fb_post_df_clean.csv',
    'ig_page': 'ig_page_df - ig_page_df.csv',
    'ig_insights': 'ig_with_insights - media_data_with_insights.csv'
}

# Load the datasets with corrected paths
fb_post_df_clean = pd.read_csv(os.path.join(directory, files['fb']))
ig_page_df = pd.read_csv(os.path.join(directory, files['ig_page']))
ig_with_insights = pd.read_csv(os.path.join(directory, files['ig_insights']))

# Print sample dates before conversion
print("\nSample dates before conversion:")
print("FB dates:", fb_post_df_clean['date'].head(2).tolist())
print("IG page dates:", ig_page_df['date'].head(2).tolist())
print("IG insights dates:", ig_with_insights['date'].head(2).tolist())

# Convert dates and normalize them (remove timezone and time information)
fb_post_df_clean['date'] = pd.to_datetime(fb_post_df_clean['date']).dt.tz_localize(None).dt.date
ig_page_df['date'] = pd.to_datetime(ig_page_df['date'], dayfirst=True).dt.date
ig_with_insights['date'] = pd.to_datetime(ig_with_insights['date']).dt.tz_localize(None).dt.date

# Convert back to datetime for proper handling
fb_post_df_clean['date'] = pd.to_datetime(fb_post_df_clean['date'])
ig_page_df['date'] = pd.to_datetime(ig_page_df['date'])
ig_with_insights['date'] = pd.to_datetime(ig_with_insights['date'])

# Print sample dates after conversion
print("\nSample dates after conversion:")
print("FB dates:", fb_post_df_clean['date'].head(2).tolist())
print("IG page dates:", ig_page_df['date'].head(2).tolist())
print("IG insights dates:", ig_with_insights['date'].head(2).tolist())

# Standardize column names to align across datasets
fb_post_df_clean.rename(columns=lambda x: x.strip().lower(), inplace=True)
ig_page_df.rename(columns=lambda x: x.strip().lower(), inplace=True)
ig_with_insights.rename(columns=lambda x: x.strip().lower(), inplace=True)

# Select common columns
common_columns = set(fb_post_df_clean.columns) & set(ig_page_df.columns) & set(ig_with_insights.columns)

# Print common columns to verify
print("\nCommon columns across datasets:", list(common_columns))

# Combine all datasets based on common columns
combined_df = pd.concat(
    [
        fb_post_df_clean[list(common_columns)],
        ig_page_df[list(common_columns)],
        ig_with_insights[list(common_columns)],
    ],
    ignore_index=True
)

# Define the output file
output_file = os.path.join(directory, 'unified_social_data.csv')

# Save the combined DataFrame to CSV
combined_df.to_csv(output_file, index=False)

# Print information about the combined dataset
print("\nDataset information:")
print(f"Total rows: {len(combined_df)}")
print(f"Columns: {list(combined_df.columns)}")
print("\nDate range:")
print(f"From: {combined_df['date'].min()}")
print(f"To: {combined_df['date'].max()}")