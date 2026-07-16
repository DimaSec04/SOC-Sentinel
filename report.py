def generate_report(results):

    report = []

    report.append("=" * 50)
    report.append("             SOC SENTINEL REPORT")
    report.append("=" * 50)

    report.append(f"Failed Login Attempts : {results['failed_logins']}")
    report.append(f"Successful Logins     : {results['successful_logins']}")
    report.append(f"Unknown Events        : {results['unknown_events']}")

    report.append("")
    report.append("Failed Users")
    report.append("-" * 50)

    for user, count in results["failed_users"].items():
        report.append(f"{user:<10} -> {count} failed attempts")

    report.append("")
    report.append("Security Alerts")
    report.append("-" * 50)

    alert = False

    for user, count in results["failed_users"].items():
        if count >= 3:
            alert = True
            report.append(
                f"ALERT: Possible Brute Force Attack on '{user}' ({count} attempts)"
            )

    if not alert:
        report.append("No Brute Force Activity Detected.")

    report.append("")
    report.append("=" * 50)
    report.append("Analysis Completed Successfully")
    report.append("=" * 50)

    for line in report:
        print(line)

    with open("report.txt", "w") as file:
        for line in report:
            file.write(line + "\n")