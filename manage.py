from flask_script import Manager, Server
from main import app, db, Annual_Full_2016

manager = Manager(app)

manager.add_command("server", Server())
@manager.shell
def make_shell_context():
	return dict(app=app, db=db, Annual_Full_2016=Annual_Full_2016)

if __name__ == "__main__":
	manager.run()