from scraper.program_scraper import ProgramScraper

url = input("Enter program URL:")

scraper = ProgramScraper(url)

text = scraper.scrape()

print(text[:1000])