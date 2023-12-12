from flask import Flask
import json

app = Flask(__name__)


@app.route('/', methods=['Get', 'POST'])
def handle_request():
    data_set = {
        "name": "Erik Tapia",
        "skills": ["React", "Angular", "JavaScript", "CSS", "Python", "HTML"],
        "work_experience": [
            {
                "position": "Software Developer Intern",
                "company": "Wells Fargo",
                "start_date": "Jan 2023",
                "end_date": "Jul 2023",
                "responsibilities": [
                    "Identified and resolved errors in the UI interface to ensure optimal user experience.",
                    "Participated in routine scrum meetings and product demos for a team of 30+ members.",
                    "Conducted comprehensive regression testing to guarantee stability, reliability, and performance quality.",
                    "Delivered project reports and milestone updates to manager in a timely manner.",
                    "Utilized frameworks and languages such as Angular, HTML, CSS, Javascript, and Typescript to modify existing and develop new applications.",
                    "Contributed to the deployment process by upgrading build packs to optimize application use."
                ]
            },
            {
                "position": "Notary Public & Center Associate",
                "company": "UPS",
                "start_date": "Sept 2020",
                "end_date": "Jun 2022",
                "responsibilities": [
                    "Diagnosed and resolved technical issues to minimize operational downtime.",
                    "Provided expert advice on both domestic and international shipments.",
                    "Trained employees on store equipment and software to streamline store operations.",
                    "Successfully notarized an average of 10-15 documents daily while maintaining client confidentiality."
                ]
            }
        ],
        "education": [
            {
                "bootcamp": "Software Development",
                "school": "Year Up",
                "graduation_date": "Sept 2023",
                "details": "200+ hours of hands-on training in software development in a year-long career development program through college-level courses and a professional six-month internship."
            },
            {
                "degree": "Associate Degree - Liberal Arts",
                "school": "Borough of Manhattan Community College",
                "graduation_date": "Jun 2016"
            }
        ]
    }

    json_dump = json.dumps(data_set)
    return json_dump
