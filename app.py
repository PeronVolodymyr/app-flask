from flask import Flask, jsonify, request

app = Flask(__name__)


students = [
    {
        'id': 1,
        'name': 'Volodymyr Peron',
        'chair': 'IFTKN',
        'group': 443
    },
    {
        'id': 2,
        'name': 'Ivan Ivanov',
        'chair': 'Computer Science',
        'group': 223
    }
]


@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify({'students': students})

@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = list(filter(lambda t: t['id'] == student_id, students))
    return jsonify({'student': student[0]})

@app.route('/api/students', methods=['POST'])
def create_student():
    student = {
        'id': students[-1]['id'] + 1,
        'name': request.json['name'],
        'chair': request.json['chair'],
        'group': request.json['group']
    }
    students.append(student)
    return jsonify({'student': student}), 201

@app.route('/api/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = list(filter(lambda t: t['id'] == student_id, students))
    student[0]['name'] = request.json.get('name', student[0]['name'])
    student[0]['chair'] = request.json.get('chair', student[0]['chair'])
    student[0]['group'] = request.json.get('group', student[0]['group'])
    return jsonify({'student': student[0]})

@app.route('/api/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    for student in students:
        if student.get('id') == student_id:
            students.remove(student)
            return jsonify({'result': True})
    return jsonify({'result': False})


if __name__ == '__main__':
    app.run()
