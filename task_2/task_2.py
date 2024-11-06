import numpy as np
from gen_random import generate_random_data

def calculate_department_threat(department_scores, importance):
    avg_threat = np.mean(department_scores)
    weighted_threat = avg_threat * importance
    return weighted_threat

def calculate_company_threat(departments):
    total_weighted_threat = 0
    total_importance = 0
    
    for department in departments:
        department_scores = department["scores"]
        importance = department["importance"]
        
        weighted_threat = calculate_department_threat(department_scores, importance)
        total_weighted_threat += weighted_threat
        total_importance += importance
    
    company_threat_score = total_weighted_threat / total_importance
    return min(max(company_threat_score, 0), 90)  

if __name__ == "__main__":
    departments_data = [
    {"scores": generate_random_data(10, 5, 50), "importance": 1},
    {"scores": generate_random_data(70, 10, 100), "importance": 4},
    {"scores": generate_random_data(60, 15, 75), "importance": 5},
    {"scores": generate_random_data(20, 5, 80), "importance": 1},
    {"scores": generate_random_data(30, 10, 30), "importance": 2}
]


    company_threat_score = calculate_company_threat(departments_data)
    for department in departments_data:
        print("Department scores:", department["scores"])
        print("Department importance:", department["importance"])
    print("Final Company Threat Score:", company_threat_score)



