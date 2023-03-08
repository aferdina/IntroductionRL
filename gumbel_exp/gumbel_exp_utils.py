import json
import scipy.stats as stats
import random
import re
import json 

def create_distributions(num_rep = 3):

    # Get a list of all distributions in scipy.stats
    distributions = [getattr(stats, name) for name in dir(
        stats) if isinstance(getattr(stats, name), stats.rv_continuous)]

    with open("gumbel_exp/bounds.json", "r") as file:
        bounds_for_parameter = json.load(file)
    
    PATTERN = r'rvs\(([^\)]+)\)'

    # get the parameter names and default values
    distribution_to_use = []
    for _ in range(num_rep):
        for dist in distributions:
            dis_use = {"parameter": {}}
            dis_use["name"] = dist.name
            dis_use["parameter"]["loc"] = 0.0
            dis_use["parameter"]["scale"] = random.uniform(0.5, 1.5)

            docstring = getattr(stats, f"{dist.name}").__doc__

            match = re.search(PATTERN, docstring)
            if match:
                params_str = match.group(1)
                params = [p.strip() for p in params_str.split(',')]
                params.remove('random_state=None')
                params.remove('size=1')
                params.remove('loc=0')
                params.remove('scale=1')
            for param in params:
                lower_bound = -50.0 if float(bounds_for_parameter[f"{dist.name}"][f"{param}"]["lower_bound"]) == float(
                    "-inf") else float(bounds_for_parameter[f"{dist.name}"][f"{param}"]["lower_bound"])
                upper_bound = 50.0 if float(bounds_for_parameter[f"{dist.name}"][f"{param}"]["upper_bound"]) == float(
                    "inf") else float(bounds_for_parameter[f"{dist.name}"][f"{param}"]["upper_bound"])

                dis_use["parameter"][param] = random.uniform(
                    lower_bound, upper_bound)

            distribution_to_use.append(dis_use)

    return distribution_to_use


def flatten_dict(d, parent_key='', sep='_'):
    """
    Flatten a dictionary of dictionaries.
    """
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

if __name__=="__main__":
    print(create_distributions(num_rep = 1))