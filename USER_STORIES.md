# TaskSphere Project User Stories

## Phase 1: Project Foundation
**User Story 1**: As a developer, I want to create a GitHub repository for the TaskSphere project so that the development team can collaborate using version control. *(High Priority)*

**User Story 2**: As a developer, I want to set up the Django REST Framework backend project so that the system can provide APIs for task management. *(High Priority)*

**User Story 3**: As a developer, I want to configure environment variables for application settings and secrets so that sensitive data is not stored in the source code. *(High Priority)*

## Phase 2: User Authentication
**User Story 4**: As a user, I want to register and log in to the system so that I can securely manage my personal tasks. *(High Priority)*

## Phase 3: Task Management Core
**User Story 5**: As a user, I want to create a task with a title and description so that I can track work I need to complete. *(High Priority)*

**User Story 6**: As a user, I want to update the status of a task (To Do, In Progress, Completed) so that I can track the progress of my work. *(High Priority)*

**User Story 7**: As a user, I want to edit existing tasks so that I can correct or update task information. *(Medium Priority)*

**User Story 8**: As a user, I want to delete completed or unnecessary tasks so that my task list remains organised. *(Medium Priority)*

## Phase 4: Frontend Development
**User Story 9**: As a developer, I want to create a React frontend application so that users can interact with the task management system through a web interface. *(High Priority)*

## Phase 5: Containerization & Deployment
**User Story 10**: As a DevOps engineer, I want to create Dockerfiles for both backend and frontend services so that the application can run in containerised environments. *(High Priority)*

**User Story 11**: As a DevOps engineer, I want to configure a GitHub Actions CI pipeline so that Docker images are automatically built when code is pushed to the repository. *(High Priority)*

## Phase 6: Development Workflow
**User Story 12**: As a DevOps engineer, I want to configure a CircleCI pipeline so that the project can support alternative CI/CD automation workflows. *(Medium Priority)*

**User Story 13**: As a developer, I want to use feature branches for development so that new features can be developed without affecting the main branch. *(Medium Priority)*

**User Story 14**: As a developer, I want to create pull requests and perform code reviews so that code quality and collaboration are improved. *(Medium Priority)*

## Phase 7: Project Management
**User Story 15**: As a project manager, I want to track development tasks on a GitHub Kanban board so that the team can monitor project progress. *(Low Priority)*

---

## Implementation Status

### ✅ Completed
- [x] **User Story 1**: GitHub repository creation (Project structure exists locally)
- [x] **User Story 2**: Django REST Framework backend project structure (Virtual environment, project setup, tasks app created)
- [x] **User Story 3**: Environment variables configuration (.env file created, settings.py updated for Vercel deployment)
- [x] **User Story 4**: User authentication (JWT-based registration, login, and profile endpoints implemented)
- [x] **User Story 5**: Task creation (Task model, serializers, and CRUD endpoints implemented)
- [x] **User Story 6**: Task status management (Status update endpoint with validation implemented)

### 🔄 In Progress  
- [ ] **User Story 7**: Task editing (Next to implement)

### ⏳ Pending
- [ ] **User Story 8**: Task deletion
- [ ] **User Story 9**: React frontend
- [ ] **User Story 10**: Dockerfiles
- [ ] **User Story 11**: GitHub Actions
- [ ] **User Story 12**: CircleCI pipeline
- [ ] **User Story 13**: Feature branching
- [ ] **User Story 14**: Pull requests
- [ ] **User Story 15**: Kanban board

---

## Project Progress Summary

### Current Status
- **Project Name**: TaskSphere
- **Backend Framework**: Django REST Framework
- **Database**: SQLite (default)
- **Virtual Environment**: ✅ Created and activated
- **Dependencies**: Django, DRF, python-decouple installed

### Completed Setup
1. ✅ Virtual environment created (`venv/`)
2. ✅ Django project structure (`task_manager/`)
3. ✅ Tasks app created (`tasks/`)
4. ✅ Requirements.txt generated
5. ✅ .gitignore configured
6. ✅ README.md with setup instructions
7. ✅ User stories organized and documented

### Next Steps
1. **Immediate**: Implement task editing functionality (User Story 7)
2. **Following**: Implement task deletion functionality

### Development Environment
- **Python**: Using `py` command
- **Django Version**: 6.0.3
- **DRF Version**: 3.16.1
- **Project Path**: `C:/Users/admin/OneDrive - Auckland Institute of Studies/Desktop/AIS/CICD/task-manager-backend`

### Commands Used
```bash
# Virtual Environment
py -m venv venv
venv\Scripts\pip.exe install django djangorestframework python-decouple

# Django Setup
venv\Scripts\django-admin.exe startproject task_manager .
venv\Scripts\django-admin.exe startapp tasks

# Dependencies
venv\Scripts\pip.exe freeze > requirements.txt
```
