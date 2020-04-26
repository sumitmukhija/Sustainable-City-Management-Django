class CronJob():

    def before_job(self):
        pass

    def after_job(self):
        pass

    def run_job(self):
        pass
    
    def exec(self):
        self.before_job()
        self.run_job()
        self.after_job()

