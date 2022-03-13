from utils import get_dict_from_json
from flask import Flask


candidates = get_dict_from_json()


app = Flask(__name__)


@app.route("/")
def show_list():
    str_candidate = "<pre>"
    for candidate in candidates.values():
        str_candidate += f"{candidate['name']}<br>{candidate['position']}<br>{candidate['skills']} <br><br>"
    str_candidate += "</pre>"
    return str_candidate


@app.route('/candidates/<int:id>')
def show_photo_and_list(id):
    candidate = candidates[id]
    str_candidate = f"<img src={candidate['picture']}></img> <br>{candidate['name']}<br>{candidate['position']}<br>{candidate['skills']} <br><br>"
    return str_candidate


@app.route('/skill/<skill>')
def show_cand_with_skill(skill):
    candidates_with_skill = "<pre>"
    for candidate in candidates.values():
        candidate_skills = candidate['skills'].split(', ')
        candidate_skills = [x.lower() for x in candidate_skills]
        if skill.lower() in candidate_skills:
            candidates_with_skill += f"{candidate['name']}<br>{candidate['position']}<br>{candidate['skills']}<br><br>"
    candidates_with_skill += "</pre>"
    return candidates_with_skill


app.run(debug=True)
