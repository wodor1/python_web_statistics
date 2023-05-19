""" import pickle

with open('./web_size.pickle', 'rb') as handle:
    sites = pickle.load(handle)

with open('./web_size_new.pickle', 'rb') as handle:
    sites_new = pickle.load(handle)

sum = 0
empty_sites = 0
print(sites[0])
print(sites_new[0]) """

# első feladat

import pickle

with open('./web_size.pickle', 'rb') as handle:
    sites = pickle.load(handle)

with open('./web_size_new.pickle', 'rb') as handle:
    sites_new = pickle.load(handle)

print(sites[0])
print(sites_new[0])

sum = 0
for site in sites:
    sum += site['size']
for site in sites_new:
    sum += site['size']

total_size_gb = round(sum / (1024), 2)  # Kb to Gb conversion
print("total size is: {} Gb".format(total_size_gb))

avg_site_size_gb = round(total_size_gb / len(sites_new), 2)
print("avg site size is: {} Gb".format(avg_site_size_gb))

# második feladat


with open('./web_size.pickle', 'rb') as handle:
    sites = pickle.load(handle)

with open('./web_size_new.pickle', 'rb') as handle:
    sites_new = pickle.load(handle)

for i in range(len(sites)):
    old_size = sites[i]['size']
    new_size = sites_new[i]['size']
    domain = sites_new[i]['domain']

    if old_size != new_size:
        difference = new_size - old_size
        change_ratio = round(difference / (new_size / 100), 2)
        print(f"{domain} changed by: {change_ratio} %")

# harmadik feladat


with open('./web_size_new.pickle', 'rb') as handle:
    sites_new = pickle.load(handle)

empty_sites = 0
for site in sites_new:
    if site['size'] == 0:
        empty_sites += 1

print("There are {} empty sites.".format(empty_sites))

# negyedik feladat


with open('./web_size_new.pickle', 'rb') as handle:
    sites_new = pickle.load(handle)

for site in sites_new:
    if site['size'] > 0:
        if site['size'] > 1024:  # size in Mb
            size_gb = round(site['size'] / 1024, 2)  # converting size to Gb
            print(f"{site['domain']} is: {size_gb} Gb")
        else:
            print(f"{site['domain']} is: {site['size']} Mb")
