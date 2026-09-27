import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    """Load the GES outstanding schools dataset into a Pandas DataFrame."""
    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    """Clean and standardize the school status values."""
    df = df.copy()

    df["Status"] = df["Status"].str.strip().str.lower()

    df["Status"] = df["Status"].replace({
        "private_registered": "Private Registered",
        "private_notregistered": "Private Not Registered",
        "public": "Public",
        "private": "Private"
    })

    return df


def filter_keta(df):
    """Filter the dataset to schools located in Keta Municipal."""
    keta_df = df[df["District"] == "Keta Municipal"].copy()
    return keta_df


def analyze_status(keta_df):
    """Count the number of Keta Municipal schools in each status category."""
    status_counts = keta_df["Status"].value_counts()
    return status_counts


def calculate_percentages(status_counts, total_schools):
    """Calculate the percentage of schools represented by each status."""
    percentages = (status_counts / total_schools) * 100
    return percentages


def get_sorted_schools(keta_df):
    """Return Keta Municipal schools sorted alphabetically by school name."""
    sorted_schools = keta_df.sort_values("School Name")
    return sorted_schools

def create_chart(status_counts):
    """Create and save a bar chart showing schools by status."""
    status_counts.plot(kind="bar")

    plt.title("Outstanding Schools in Keta Municipal by Status")
    plt.xlabel("School Status")
    plt.ylabel("Number of Schools")
    plt.xticks(rotation=0)

    plt.tight_layout()
    plt.savefig("keta_school_status.png")
    plt.close()


def main():
    """Run the complete Keta Municipal school data analysis."""

    file_path = "data/outstanding_schools_2025.csv"

    df = load_data(file_path)
    df = clean_data(df)
    keta_df = filter_keta(df)

    status_counts = analyze_status(keta_df)

    total_schools = len(keta_df)
    percentages = calculate_percentages(
        status_counts,
        total_schools
    )

    # Create a summary table for the analysis results
    summary = pd.DataFrame({
        "School Status": status_counts.index,
        "Number of Schools": status_counts.values,
        "Percentage": percentages.values
    })

    summary["Percentage"] = summary["Percentage"].round(1)

    sorted_schools = get_sorted_schools(keta_df)
    create_chart(status_counts)

    print("GES OUTSTANDING SCHOOLS DATA ANALYSIS")
    print("=" * 45)

    print(f"\nTotal Keta Municipal schools: {total_schools}")

    print("\nQuestion 1:")
    print(
        "How many outstanding schools in Keta Municipal "
        "are Public and Private Registered?"
    )
    print(
        f"Private Registered schools: "
        f"{status_counts.get('Private Registered', 0)}"
    )
    print(
        f"Public schools: "
        f"{status_counts.get('Public', 0)}"
    )

    print("\nQuestion 2:")
    print(
        "What percentage of outstanding schools in Keta Municipal "
        "are Private Registered and Public?"
    )
    print(
        f"Private Registered: "
        f"{percentages.get('Private Registered', 0):.1f}%"
    )
    print(
        f"Public: "
        f"{percentages.get('Public', 0):.1f}%"
    )

    print("\nSummary Table:")
    print(summary.to_string(index=False))

    print("\nQuestion 3:")
    print(
        "What are the names of the outstanding schools in Keta Municipal, "
        "sorted alphabetically?"
    )

    for school in sorted_schools["School Name"]:
        print(school)


if __name__ == "__main__":
    main()
