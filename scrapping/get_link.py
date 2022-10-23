import advertools as adv
import pandas as pd


url = 'https://www.royco.co.id/sitemap.xml'

royco_sitemap = adv.sitemap_to_df(url)
masakapa_sitemaps = adv.sitemap_to_df('https://www.masakapahariini.com/recipe-sitemap1.xml')
masakapa_sitemapss = adv.sitemap_to_df('https://www.masakapahariini.com/recipe-sitemap2.xml')

#cleaning
royco_clean = royco_sitemap[royco_sitemap['loc'].str.contains('Ide-Resep') == True]

#merging
masakapa_clean = pd.concat([masakapa_sitemaps, masakapa_sitemapss])

#save to csv
royco_clean.to_csv('files/royco_links.csv', index=False)
masakapa_clean.to_csv('files/masakapa_links.csv', index=False)