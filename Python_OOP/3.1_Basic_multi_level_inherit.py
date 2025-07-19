class platform:
    def show(self):
        print("This is fetquest Platform")

class project_stockScreener(platform):  #this will have access to show and display_projects
    def display_projects(self):
        print("fetquest Stock Screener")

class project_expenseTracker(project_stockScreener): #this will have access to show, display_projects and display_discription
    def display_discription(self):
        print("ExpenseTracker")

tracker =  project_expenseTracker()
tracker.display_projects()
tracker.show()