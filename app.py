from scraper.program_scraper import ProgramScraper
from analyzer.scope_analyzer import find_vulnerabilities
from recommender.tool_mapper import recommend_tools


def main():

    print("=== ScopeSage AI Bug Bounty Assistant ===")

    url = input("Enter Bug Bounty Program URL: ")

    scraper = ProgramScraper(url)

    print("\nScraping program page...")
    text = scraper.scrape()

    print("Analyzing vulnerabilities...")
    vulns = find_vulnerabilities(text)

    if not vulns:
        print("No common vulnerabilities detected in policy text")
        return

    print("\nAllowed Vulnerabilities Detected:")

    for v in vulns:
        print(f"- {v}")

    print("\nRecommended Tools:")

    tools = recommend_tools(vulns)

    for vuln, tool_list in tools.items():
        print(f"\n{vuln}")
        for tool in tool_list:
            print(f"  - {tool}")


if __name__ == "__main__":
    main()