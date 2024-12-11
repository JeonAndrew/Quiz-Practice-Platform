import firebase_admin
from firebase_admin import credentials, firestore

# Replace this with your service account key path
service_account_path = '/Users/aummaneni/Quiz-Practice-Platform-1/quiz-backend/src/cs222-quiz-proj-firebase-adminsdk-k0qc4-936c2f1d05.json'

cred = credentials.Certificate(service_account_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

def initialize_firestore_data(db):
    # Define courses, topics, and questions
    # Structure:
    # courses = {
    #   "CS 225": {
    #       "course_id": "225",
    #       "topics": [
    #           {
    #               "topic_id": 1,
    #               "name": "Arrays",
    #               "questions": [
    #                   { "question": "...", "options": [...], "correct_answer": "..." },
    #                   ...
    #               ]
    #           },
    #           ...
    #       ]
    #   },
    #   ...
    # }

    courses = {
        "CS 225": {
            "course_id": "225",
            "topics": [
                {
                    "topic_id": 1,
                    "name": "Arrays",
                    "questions": [
                        {
                            "question": "What is the time complexity of accessing an element by index in a static array?",
                            "options": ["O(1)", "O(n)", "O(log n)"],
                            "correct_answer": "O(1)"
                        },
                        {
                            "question": "Which of the following best describes a dynamic array?",
                            "options": ["A linked list with random access", "An array that can resize itself", "A binary tree stored in memory"],
                            "correct_answer": "An array that can resize itself"
                        },
                        {
                            "question": "What happens when you exceed the current capacity of a dynamic array during an insertion?",
                            "options": ["It causes a segmentation fault", "It automatically resizes and copies elements to a new array", "It discards the insertion"],
                            "correct_answer": "It automatically resizes and copies elements to a new array"
                        },
                        {
                            "question": "What is the time complexity of inserting at the end of a dynamic array (amortized)?",
                            "options": ["O(1)", "O(n)", "O(log n)"],
                            "correct_answer": "O(1)"
                        },
                        {
                            "question": "How are array elements stored in memory?",
                            "options": ["Contiguously", "Randomly scattered", "In a linked structure"],
                            "correct_answer": "Contiguously"
                        },
                    ]
                },
                {
                    "topic_id": 2,
                    "name": "Linked Lists",
                    "questions": [
                        {
                            "question": "What is the time complexity of inserting at the front of a singly linked list?",
                            "options": ["O(1)", "O(n)", "O(log n)"],
                            "correct_answer": "O(1)"
                        },
                        {
                            "question": "Which operation is expensive in a singly linked list?",
                            "options": ["Accessing the first element", "Accessing the last element", "Inserting at the head"],
                            "correct_answer": "Accessing the last element"
                        },
                        {
                            "question": "What is typically stored in a node of a singly linked list?",
                            "options": ["Data and a pointer/reference to the next node", "Data only", "Data and pointers to both next and previous nodes"],
                            "correct_answer": "Data and a pointer/reference to the next node"
                        },
                        {
                            "question": "How do you find the length of a singly linked list?",
                            "options": ["By keeping a length counter", "By traversing through the list", "By accessing the last node's index"],
                            "correct_answer": "By traversing through the list"
                        },
                        {
                            "question": "What advantage do doubly linked lists have over singly linked lists?",
                            "options": ["Constant time insertion at the head only", "Easier backward traversal", "They use less memory"],
                            "correct_answer": "Easier backward traversal"
                        },
                    ]
                },
                {
                    "topic_id": 3,
                    "name": "Trees",
                    "questions": [
                        {
                            "question": "What is a binary tree?",
                            "options": ["A tree with at most two children per node", "A tree with sorted elements", "A tree with nodes of degree two always"],
                            "correct_answer": "A tree with at most two children per node"
                        },
                        {
                            "question": "What is the average time complexity of search in a balanced binary search tree?",
                            "options": ["O(n)", "O(log n)", "O(1)"],
                            "correct_answer": "O(log n)"
                        },
                        {
                            "question": "Which traversal of a BST yields a sorted order of elements?",
                            "options": ["Pre-order", "In-order", "Post-order"],
                            "correct_answer": "In-order"
                        },
                        {
                            "question": "What is a leaf node?",
                            "options": ["A node with no children", "A node with one child", "The root node of the tree"],
                            "correct_answer": "A node with no children"
                        },
                        {
                            "question": "Which of the following is a self-balancing tree?",
                            "options": ["AVL Tree", "Simple BST", "Linked list"],
                            "correct_answer": "AVL Tree"
                        },
                    ]
                }
            ]
        },
        "CS 374": {
            "course_id": "374",
            "topics": [
                {
                    "topic_id": 1,
                    "name": "Graphs",
                    "questions": [
                        {
                            "question": "What is a graph?",
                            "options": ["A collection of nodes and edges", "A type of tree structure", "A line plot of data"],
                            "correct_answer": "A collection of nodes and edges"
                        },
                        {
                            "question": "What is the time complexity of DFS on a graph with V vertices and E edges?",
                            "options": ["O(V+E)", "O(V*E)", "O(V^2)"],
                            "correct_answer": "O(V+E)"
                        },
                        {
                            "question": "Which data structure is typically used to implement BFS?",
                            "options": ["Stack", "Queue", "Hash Map"],
                            "correct_answer": "Queue"
                        },
                        {
                            "question": "What is a connected graph?",
                            "options": ["A graph with no edges", "A graph where there's a path between every pair of vertices", "A graph that is also a tree"],
                            "correct_answer": "A graph where there's a path between every pair of vertices"
                        },
                        {
                            "question": "Which algorithm finds the shortest path in an unweighted graph?",
                            "options": ["Dijkstra's algorithm", "Bellman-Ford algorithm", "BFS"],
                            "correct_answer": "BFS"
                        },
                    ]
                },
                {
                    "topic_id": 2,
                    "name": "Dynamic Programming",
                    "questions": [
                        {
                            "question": "Dynamic Programming is a technique primarily used to:",
                            "options": ["Break problems into smaller subproblems and store solutions", "Sort arrays efficiently", "Perform binary searches"],
                            "correct_answer": "Break problems into smaller subproblems and store solutions"
                        },
                        {
                            "question": "Which approach is commonly used in DP?",
                            "options": ["Top-down memoization or bottom-up tabulation", "Greedy choice at every step", "Divide and conquer without memoization"],
                            "correct_answer": "Top-down memoization or bottom-up tabulation"
                        },
                        {
                            "question": "What is the main benefit of using DP?",
                            "options": ["Reducing time complexity by avoiding recomputation", "Reducing space complexity drastically", "Making the code more readable"],
                            "correct_answer": "Reducing time complexity by avoiding recomputation"
                        },
                        {
                            "question": "Fibonacci sequence calculation using DP has what time complexity?",
                            "options": ["O(n)", "O(log n)", "O(n^2)"],
                            "correct_answer": "O(n)"
                        },
                        {
                            "question": "Which type of problems are well-suited for DP?",
                            "options": ["Problems with overlapping subproblems and optimal substructure", "Problems that cannot be broken into subproblems", "Problems where greedy solution is always optimal"],
                            "correct_answer": "Problems with overlapping subproblems and optimal substructure"
                        },
                    ]
                },
                {
                    "topic_id": 3,
                    "name": "Complexity",
                    "questions": [
                        {
                            "question": "What does Big-O notation describe?",
                            "options": ["The exact running time of an algorithm", "The upper bound on the growth rate of the runtime", "The memory usage of an algorithm"],
                            "correct_answer": "The upper bound on the growth rate of the runtime"
                        },
                        {
                            "question": "What is the time complexity of binary search?",
                            "options": ["O(n)", "O(log n)", "O(1)"],
                            "correct_answer": "O(log n)"
                        },
                        {
                            "question": "Which complexity class describes decision problems solvable in polynomial time?",
                            "options": ["P", "NP", "EXP"],
                            "correct_answer": "P"
                        },
                        {
                            "question": "What does NP stand for?",
                            "options": ["Non-Polynomial", "Non-deterministic Polynomial-time", "Negative Polynomial-time"],
                            "correct_answer": "Non-deterministic Polynomial-time"
                        },
                        {
                            "question": "If a problem is in NP and in co-NP, it is believed that:",
                            "options": ["P = NP", "The problem is in P", "Nothing can be inferred"],
                            "correct_answer": "Nothing can be inferred"
                        },
                    ]
                }
            ]
        },
        "CS 233": {
            "course_id": "233",
            "topics": [
                {
                    "topic_id": 1,
                    "name": "CPU",
                    "questions": [
                        {
                            "question": "What does CPU stand for?",
                            "options": ["Central Processing Unit", "Computer Power Unit", "Central Print Unit"],
                            "correct_answer": "Central Processing Unit"
                        },
                        {
                            "question": "Which part of the CPU performs arithmetic and logical operations?",
                            "options": ["Control Unit", "ALU", "Register File"],
                            "correct_answer": "ALU"
                        },
                        {
                            "question": "What is the role of the Control Unit?",
                            "options": ["Executing arithmetic", "Directing operations of the processor", "Storing instructions permanently"],
                            "correct_answer": "Directing operations of the processor"
                        },
                        {
                            "question": "What is a register?",
                            "options": ["A small, fast memory location inside the CPU", "A large memory module external to the CPU", "A disk drive"],
                            "correct_answer": "A small, fast memory location inside the CPU"
                        },
                        {
                            "question": "What is the clock speed of a CPU measured in?",
                            "options": ["Hertz (Hz)", "Bytes (B)", "Instructions per second"],
                            "correct_answer": "Hertz (Hz)"
                        },
                    ]
                },
                {
                    "topic_id": 2,
                    "name": "Memory",
                    "questions": [
                        {
                            "question": "What is the fastest form of memory typically available to the CPU?",
                            "options": ["Cache memory", "RAM", "Hard Drive"],
                            "correct_answer": "Cache memory"
                        },
                        {
                            "question": "What is the role of DRAM in a computer system?",
                            "options": ["Long-term storage of files", "Volatile main memory", "Permanent memory integrated in CPU"],
                            "correct_answer": "Volatile main memory"
                        },
                        {
                            "question": "Which memory type retains data without power?",
                            "options": ["RAM", "ROM/Flash memory", "SRAM"],
                            "correct_answer": "ROM/Flash memory"
                        },
                        {
                            "question": "What is virtual memory?",
                            "options": ["An abstraction of main memory that uses disk storage to appear larger", "A memory type that does not physically exist", "Memory stored in the GPU"],
                            "correct_answer": "An abstraction of main memory that uses disk storage to appear larger"
                        },
                        {
                            "question": "Cache hit occurs when:",
                            "options": ["The requested data is found in cache", "The requested data is not in the cache", "Data is lost during a read"],
                            "correct_answer": "The requested data is found in cache"
                        },
                    ]
                },
                {
                    "topic_id": 3,
                    "name": "Parallelism",
                    "questions": [
                        {
                            "question": "What is parallelism in computing?",
                            "options": ["Executing multiple operations simultaneously", "Running only one operation at a time", "Turning off multiple CPU cores"],
                            "correct_answer": "Executing multiple operations simultaneously"
                        },
                        {
                            "question": "Which of the following is a model for parallel computing?",
                            "options": ["MapReduce", "Bubble Sort", "Binary Search"],
                            "correct_answer": "MapReduce"
                        },
                        {
                            "question": "What is a race condition?",
                            "options": ["A situation where two operations compete and the outcome depends on timing", "A condition that speeds up computation", "A GPU-only problem"],
                            "correct_answer": "A situation where two operations compete and the outcome depends on timing"
                        },
                        {
                            "question": "What does SIMD stand for?",
                            "options": ["Single Instruction, Multiple Data", "Single Instruction, Multiple Devices", "Sequential Instructions, Multiplying Data"],
                            "correct_answer": "Single Instruction, Multiple Data"
                        },
                        {
                            "question": "What is a common challenge of parallel computing?",
                            "options": ["Achieving linear speedup with more processors", "Ensuring no process runs at all", "Making memory access slower"],
                            "correct_answer": "Achieving linear speedup with more processors"
                        },
                    ]
                }
            ]
        }
    }

    # Populate Firestore
    for course_name, course_data in courses.items():
        course_id = course_data['course_id']
        course_ref = db.collection('courses').document(course_id)
        course_ref.set({
            'name': course_name
        })
        for topic_data in course_data['topics']:
            topic_id_str = str(topic_data['topic_id'])
            topic_ref = course_ref.collection('topics').document(topic_id_str)
            topic_ref.set({
                'name': topic_data['name'],
                'proficiency': 10,
                'active': True
            })

            # Add questions
            for i, q in enumerate(topic_data['questions'], start=1):
                q_id_str = str(i)
                question_ref = topic_ref.collection('questions').document(q_id_str)
                question_ref.set({
                    'question': q['question'],
                    'options': q['options'],
                    'correct_answer': q['correct_answer']
                })

    print("Firestore initialization complete with sample courses, topics, and questions.")

if __name__ == "__main__":
    initialize_firestore_data(db)