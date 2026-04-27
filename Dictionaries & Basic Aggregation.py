# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cybersecurity": 225,
    "Cloud Consulting": 200,
    "Technical Support": 95
}

customer1 = {
    "company_name": "Alpha Innovations",
    "contact_person": "Sarah Johnson",
    "email": "sarah@alphainnovations.com",
    "phone": "555-1001"
}

customer2 = {
    "company_name": "BrightPath Logistics",
    "contact_person": "Michael Lee",
    "email": "michael@brightpathlogistics.com",
    "phone": "555-1002"
}

customer3 = {
    "company_name": "Summit Retail Group",
    "contact_person": "Emily Carter",
    "email": "emily@summitretail.com",
    "phone": "555-1003"
}

customer4 = {
    "company_name": "NextGen Health",
    "contact_person": "David Brown",
    "email": "david@nextgenhealth.com",
    "phone": "555-1004"
}

customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

print("\nAll Customers:")
print("-" * 60)
for customer_id, info in customers.items():
    print(f"{customer_id}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print()

c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("\n\nCustomer Lookups:")
print("-" * 60)
print("C002 Information:", c002_info)
print("C003 Contact Person:", c003_contact)
print("C999 Lookup:", c999_info)

customers["C001"]["phone"] = "555-9001"
customers["C002"]["industry"] = "Transportation"

print("\n\nUpdating Customer Information:")
print("-" * 60)
print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])

projects = {
    "C001": [
        {"name": "Company Website Redesign", "service": "Web Development", "hours": 120, "budget": 18000},
        {"name": "Cloud Migration", "service": "Cloud Consulting", "hours": 80, "budget": 16000}
    ],
    "C002": [
        {"name": "Logistics Dashboard", "service": "Data Analysis", "hours": 90, "budget": 15750}
    ],
    "C003": [
        {"name": "Security Audit", "service": "Cybersecurity", "hours": 60, "budget": 13500},
        {"name": "Help Desk Setup", "service": "Technical Support", "hours": 40, "budget": 3800}
    ],
    "C004": [
        {"name": "Patient Portal", "service": "Web Development", "hours": 150, "budget": 22500}
    ]
}

print("\n\nProject Information:")
print("-" * 60)
for customer_id, project_list in projects.items():
    print(f"{customer_id}:")
    for project in project_list:
        print(f"  {project}")
    print()

print("\n\nProject Cost Calculations:")
print("-" * 60)
for customer_id, project_list in projects.items():
    for project in project_list:
        hourly_rate = services[project["service"]]
        cost = hourly_rate * project["hours"]
        print(f"{customer_id} - {project['name']}:")
        print(f"  Service: {project['service']}")
        print(f"  Hours: {project['hours']}")
        print(f"  Hourly Rate: ${hourly_rate}")
        print(f"  Calculated Cost: ${cost}")
        print(f"  Budget: ${project['budget']}")
        print()

print("\n\nCustomer Statistics:")
print("-" * 60)
print("Customer IDs:", list(customers.keys()))
print("Customer Companies:", [customer["company_name"] for customer in customers.values()])
print("Total Customers:", len(customers))

service_counts = {}

for project_list in projects.values():
    for project in project_list:
        service = project["service"]
        service_counts[service] = service_counts.get(service, 0) + 1

print("\n\nService Usage Analysis:")
print("-" * 60)
for service, count in service_counts.items():
    print(f"{service}: {count}")

all_projects = [project for project_list in projects.values() for project in project_list]

total_hours = sum(project["hours"] for project in all_projects)
total_budget = sum(project["budget"] for project in all_projects)
avg_budget = total_budget / len(all_projects) if all_projects else 0
max_budget = max(project["budget"] for project in all_projects) if all_projects else 0
min_budget = min(project["budget"] for project in all_projects) if all_projects else 0

most_expensive_project = max(all_projects, key=lambda p: p["budget"]) if all_projects else None
least_expensive_project = min(all_projects, key=lambda p: p["budget"]) if all_projects else None

print("\n\nFinancial Summary:")
print("-" * 60)
print("Total Hours:", total_hours)
print("Total Budget: $", total_budget)
print("Average Project Budget: $", avg_budget)
print("Max Budget: $", max_budget)
print("Min Budget: $", min_budget)
print("Most Expensive Project:", most_expensive_project)
print("Least Expensive Project:", least_expensive_project)

print("\n\nCustomer Summary Report:")
print("-" * 60)
for customer_id, customer_info in customers.items():
    customer_projects = projects.get(customer_id, [])
    num_projects = len(customer_projects)
    customer_hours = sum(project["hours"] for project in customer_projects)
    customer_budget = sum(project["budget"] for project in customer_projects)

    print(f"{customer_id} - {customer_info['company_name']}")
    print(f"  Contact: {customer_info['contact_person']}")
    print(f"  Email: {customer_info['email']}")
    print(f"  Phone: {customer_info['phone']}")
    print(f"  Number of Projects: {num_projects}")
    print(f"  Total Hours: {customer_hours}")
    print(f"  Total Budget: ${customer_budget}")
    print()

adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
for service, rate in adjusted_rates.items():
    print(f"{service}: ${rate:.2f}")

active_customers = {cid: info for cid, info in customers.items() if cid in projects and len(projects[cid]) > 0}

print("\n\nActive Customers (with projects):")
print("-" * 60)
for cid, info in active_customers.items():
    print(f"{cid}: {info['company_name']}")

customer_budgets = {cid: sum(project["budget"] for project in project_list) for cid, project_list in projects.items()}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
for cid, budget in customer_budgets.items():
    print(f"{cid}: ${budget}")

service_tiers = {
    service: "Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic"
    for service, rate in services.items()
}

print("\n\nService Pricing Tiers:")
print("-" * 60)
for service, tier in service_tiers.items():
    print(f"{service}: {tier}")

def validate_customer(customer_dict):
    required_fields = ["company_name", "contact_person", "email", "phone"]
    for field in required_fields:
        if field not in customer_dict or not customer_dict[field]:
            return False
    return True

print("\n\nCustomer Validation:")
print("-" * 60)
for customer_id, customer_info in customers.items():
    print(f"{customer_id}: {validate_customer(customer_info)}")

statuses = ["active", "completed", "pending"]
status_counts = {"active": 0, "completed": 0, "pending": 0}

project_number = 0
for project_list in projects.values():
    for project in project_list:
        project["status"] = statuses[project_number % len(statuses)]
        status_counts[project["status"]] += 1
        project_number += 1

print("\n\nProject Status Summary:")
print("-" * 60)
for status, count in status_counts.items():
    print(f"{status.title()}: {count}")

def analyze_customer_budgets(projects_dict):
    budget_analysis = {}

    for customer_id, project_list in projects_dict.items():
        total = sum(project["budget"] for project in project_list)
        count = len(project_list)
        average = total / count if count > 0 else 0

        budget_analysis[customer_id] = {
            "total": total,
            "average": average,
            "count": count
        }

    return budget_analysis

budget_analysis = analyze_customer_budgets(projects)

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
for customer_id, stats in budget_analysis.items():
    print(f"{customer_id}: {stats}")

def recommend_services(customer_id, customers, projects, services):
    customer_projects = projects.get(customer_id, [])
    used_services = set()

    for project in customer_projects:
        used_services.add(project["service"])

    unused_services = []
    for service in services:
        if service not in used_services:
            unused_services.append(service)

    if customer_projects:
        avg_budget = sum(project["budget"] for project in customer_projects) / len(customer_projects)
    else:
        avg_budget = 0

    recommended = []
    for service in unused_services:
        rate = services[service]
        estimated_cost = rate * 50 

        if avg_budget == 0 or estimated_cost <= avg_budget * 1.2:
            recommended.append(service)

    return recommended

print("\n\nService Recommendations:")
print("-" * 60)
for customer_id in customers:
    recommendations = recommend_services(customer_id, customers, projects, services)
    print(f"{customer_id} ({customers[customer_id]['company_name']}): {recommendations}")