[33mcommit d661f24df226c10233eafa79893f046349452e38[m[33m ([m[1;36mHEAD -> [m[1;32mdesktop[m[33m, [m[1;31mupstream/desktop[m[33m, [m[1;31morigin/desktop[m[33m)[m
Author: eyko139 <mud2@gmx.de>
Date:   Sun May 16 13:45:24 2021 +0200

    Added todo comment section

[1mdiff --git a/app/main/views.py b/app/main/views.py[m
[1mindex 0e98318..2f420cc 100755[m
[1m--- a/app/main/views.py[m
[1m+++ b/app/main/views.py[m
[36m@@ -4,10 +4,10 @@[m [mfrom werkzeug.utils import secure_filename[m
 from .. import db[m
 from . import main[m
 from .forms import SubmitForm[m
[31m-from ..models import Todo[m
[32m+[m[32mfrom ..models import Todo, Post[m
 from datetime import datetime[m
 from .. import moment[m
[31m-from flask_login import login_required[m
[32m+[m[32mfrom flask_login import login_required, current_user[m
 from ..models import User[m
 [m
 UPLOAD_FOLDER = "~/Projects"[m
[36m@@ -44,7 +44,7 @@[m [mdef adder():[m
 @login_required[m
 def list():[m
     todos=Todo.query.all()[m
[31m-[m
[32m+[m[32m    posts = Post.query.all()[m
     if request.method == "POST":[m
         if request.form.get("delete"):[m
                 will_delete = Todo.query.filter_by(id=request.form["delete"]).first()[m
[36m@@ -57,10 +57,19 @@[m [mdef list():[m
                 finished_todo.status = True[m
                 finished_todo.completion_time = datetime.now() [m
                 db.session.commit()[m
[31m-                flash("Finished Todo")[m
[32m+[m[32m                flash("Finished Todo", "completed")[m
                 return redirect(url_for("main.list"))[m
 [m
[31m-    return render_template("list.html", todos=todos, current_time=datetime.utcnow()) [m
[32m+[m[32m        if "post_comment" in request.form:[m
[32m+[m[32m                post = Post(body=request.form["comment_body"],[m
[32m+[m[32m                            author=current_user._get_current_object())[m
[32m+[m[32m                db.session.add(post)[m
[32m+[m[32m                db.session.commit()[m
[32m+[m[32m                flash("Added comment", "add")[m
[32m+[m[32m                return redirect(url_for("main.list"))[m
[32m+[m[41m        [m
[32m+[m
[32m+[m[32m    return render_template("list.html", todos=todos, current_time=datetime.utcnow(), posts=posts)[m[41m [m
 [m
 @main.route("/completed", methods = ["GET", "POST"])[m
 @login_required[m
[1mdiff --git a/app/models.py b/app/models.py[m
[1mindex 86bbc56..609ad74 100755[m
[1m--- a/app/models.py[m
[1m+++ b/app/models.py[m
[36m@@ -16,6 +16,7 @@[m [mclass Role(db.Model):[m
         return "{}".format(self.name)[m
     [m
 class User(UserMixin, db.Model):[m
[32m+[m[32m    __tablename__= "users"[m
     id = db.Column(db.Integer, primary_key=True)[m
     username = db.Column(db.String(128), unique=True, index=True)[m
     email = db.Column(db.String(128), unique=True, index=True)[m
[36m@@ -24,7 +25,8 @@[m [mclass User(UserMixin, db.Model):[m
     confirmed = db.Column(db.Boolean, default=False)[m
     member_since = db.Column(db.DateTime(), default=datetime.datetime.now)[m
     about_me = db.Column(db.Text())[m
[31m-[m
[32m+[m[32m    posts = db.relationship("Post", backref="author", lazy="dynamic")[m
[32m+[m[41m    [m
     def __repr__(self):[m
         return "User:{}, email: {}, role: {}".format(self.username, self.email, self.role_id)[m
     @property[m
[36m@@ -77,4 +79,12 @@[m [mclass Todo(db.Model):[m
 [m
 [m
 #this is even worse[m
[31m-[m
[32m+[m[32mclass Post(db.Model):[m
[32m+[m[32m    __tablename__ = "posts"[m
[32m+[m[32m    id = db.Column(db.Integer, primary_key=True)[m
[32m+[m[32m    body = db.Column(db.Text)[m
[32m+[m[32m    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.now)[m
[32m+[m[32m    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))[m
[32m+[m[41m    [m
[32m+[m[32m    def __repr__(self):[m
[32m+[m[32m        return "Post_id: {}, Author: {}, Body: {}".format(self.id, self.author_id, self.body)[m
[1mdiff --git a/app/templates/list.html b/app/templates/list.html[m
[1mindex 92dbc4f..ff73a6c 100755[m
[1m--- a/app/templates/list.html[m
[1m+++ b/app/templates/list.html[m
[36m@@ -27,7 +27,18 @@[m
                                      </script>[m
       </div>[m
       {% endif %}[m
[31m-      {% if category != "error" %}[m
[32m+[m[32m      {% if category == "add" %}[m
[32m+[m[32m      <div class="alert alert-success" role="alert">[m
[32m+[m[32m              <h4 class="alert-heading">{{ message }}</h4>[m
[32m+[m[32m                                      <script>[m[41m [m
[32m+[m[32m                                        function mom() {[m
[32m+[m[32m                                        var Now = moment();[m
[32m+[m[32m                                        var eDisplayMoment = document.getElementById("displayMoment").innerHTML = Now;[m
[32m+[m[32m                                            }[m
[32m+[m[32m                                     </script>[m
[32m+[m[32m      </div>[m
[32m+[m[32m      {% endif %}[m
[32m+[m[32m      {% if category == "completed"  %}[m
       <div class="alert alert-success" role="alert">[m
               <h4 class="alert-heading">{{ message }}</h4>[m
                                       <script> [m
[36m@@ -98,6 +109,31 @@[m
                                   <button type="submit" class="btn btn-success btn-sm font-size:1rem" name="done" value="{{ todo.id }}">Done</button>[m
                           </form>[m
         </div>[m
[32m+[m[32m        <div class="row">[m
[32m+[m[32m            <h2>Comments</h2>[m
[32m+[m[32m        </div>[m[41m  [m
[32m+[m[32m        <div class="row">[m
[32m+[m[32m          <div class="container pt-5">[m
[32m+[m[32m            <div class="list-group">[m
[32m+[m[32m              {% for post in posts %}[m
[32m+[m[32m                <div class"list-group-item my-item">[m
[32m+[m[32m                  <h4 class="bg-light">{{ post.author.username }} <span style="font-size: 15px">- {{ post.timestamp.strftime("%d. %b %Y %H:%M") }}</span></h4><br>[m[41m [m
[32m+[m[32m                  <p> {{ post.body }} </p>[m
[32m+[m[32m                </div>[m
[32m+[m[32m              {% endfor %}[m
[32m+[m[32m            </div>[m
[32m+[m[32m          </div>[m
[32m+[m[32m        </div>[m
[32m+[m[32m        <div class="row">[m
[32m+[m[32m          <div class="container pt-5">[m
[32m+[m[32m            <form method="post">[m
[32m+[m[32m              <div class="mb-3">[m
[32m+[m[32m                <textarea class="form-control" name="comment_body" placeholder="Leave a comment"></textarea>[m
[32m+[m[32m                <button type="submit" class="btn btn-primary" name="post_comment">Add comment</button>[m
[32m+[m[32m              </div>[m
[32m+[m[32m            </form>[m
[32m+[m[32m          </div>[m
[32m+[m[32m        </div>[m
       </div>[m
       </div>[m
     </div>[m
[1mdiff --git a/bibi.db b/bibi.db[m
[1mindex f9a449f..1856f54 100755[m
Binary files a/bibi.db and b/bibi.db differ
[1mdiff --git a/bin/Activate.ps1 b/bin/Activate.ps1[m
[1mold mode 100755[m
[1mnew mode 100644[m
[1mdiff --git a/bin/activate b/bin/activate[m
[1mold mode 100755[m
[1mnew mode 100644[m
[1mindex 0a795af..847d4c9[m
[1m--- a/bin/activate[m
[1m+++ b/bin/activate[m
[36m@@ -37,7 +37,7 @@[m [mdeactivate () {[m
 # unset irrelevant variables[m
 deactivate nondestructive[m
 [m
[31m-VIRTUAL_ENV="/home/a/Projects/todo"[m
[32m+[m[32mVIRTUAL_ENV="/home/s/Projects/melonpage/melonpage"[m
 export VIRTUAL_ENV[m
 [m
 _OLD_VIRTUAL_PATH="$PATH"[m
[36m@@ -54,7 +54,7 @@[m [mfi[m
 [m
 if [ -z "${VIRTUAL_ENV_DISABLE_PROMPT:-}" ] ; then[m
     _OLD_VIRTUAL_PS1="${PS1:-}"[m
[31m-    PS1="(todo) ${PS1:-}"[m
[32m+[m[32m    PS1="(melonpage) ${PS1:-}"[m
     export PS1[m
 fi[m
 [m
[1mdiff --git a/bin/activate.csh b/bin/activate.csh[m
[1mold mode 100755[m
[1mnew mode 100644[m
[1mindex 7738bce..6a3a724[m
[1m--- a/bin/activate.csh[m
[1m+++ b/bin/activate.csh[m
[36m@@ -8,7 +8,7 @@[m [malias deactivate 'test $?_OLD_VIRTUAL_PATH != 0 && setenv PATH "$_OLD_VIRTUAL_PA[m
 # Unset irrelevant variables.[m
 deactivate nondestructive[m
 [m
[31m-setenv VIRTUAL_ENV "/home/a/Projects/todo"[m
[32m+[m[32msetenv VIRTUAL_ENV "/home/s/Projects/melonpage/melonpage"[m
 [m
 set _OLD_VIRTUAL_PATH="$PATH"[m
 setenv PATH "$VIRTUAL_ENV/bin:$PATH"[m
[36m@@ -17,7 +17,7 @@[m [msetenv PATH "$VIRTUAL_ENV/bin:$PATH"[m
 set _OLD_VIRTUAL_PROMPT="$prompt"[m
 [m
 if (! "$?VIRTUAL_ENV_DISABLE_PROMPT") then[m
[31m-    set prompt = "(todo) $prompt"[m
[32m+[m[32m    set prompt = "(melonpage) $prompt"[m
 endif[m
 [m
 alias pydoc python -m pydoc[m
[1mdiff --git a/bin/activate.fish b/bin/activate.fish[m
[1mold mode 100755[m
[1mnew mode 100644[m
[1mindex dc32e6d..adb2b8d[m
[1m--- a/bin/activate.fish[m
[1m+++ b/bin/activate.fish[m
[36m@@ -29,7 +29,7 @@[m [mend[m
 # Unset irrelevant variables.[m
 deactivate nondestructive[m
 [m
[31m-set -gx VIRTUAL_ENV "/home/a/Projects/todo"[m
[32m+[m[32mset -gx VIRTUAL_ENV "/home/s/Projects/melonpage/melonpage"[m
 [m
 set -gx _OLD_VIRTUAL_PATH $PATH[m
 set -gx PATH "$VIRTUAL_ENV/bin" $PATH[m
[36m@@ -52,7 +52,7 @@[m [mif test -z "$VIRTUAL_ENV_DISABLE_PROMPT"[m
         set -l old_status $status[m
 [m
         # Output the venv prompt; color taken from the blue of the Python logo.[m
[31m-        printf "%s%s%s" (set_color 4B8BBE) "(todo) " (set_color normal)[m
[32m+[m[32m        printf "%s%s%s" (set_color 4B8BBE) "(melonpage) " (set_color normal)[m
 [m
         # Restore the return status of the previous command.[m
         echo "exit $old_status" | .[m
[1mdiff --git a/bin/alembic b/bin/alembic[m
[1mindex c058ac8..165891e 100755[m
[1m--- a/bin/alembic[m
[1m+++ b/bin/alembic[m
[36m@@ -1,4 +1,4 @@[m
[31m-#!/home/a/Projects/git-todo/melonpage/bin/python[m
[32m+[m[32m#!/home/s/Projects/melonpage/melonpage/bin/python[m
 # -*- coding: utf-8 -*-[m
 import re[m
 import sys[m
[1mdiff --git a/bin/easy_install b/bin/easy_install[m
[1mindex 27fc112..473e262 100755[m
[1m--- a/bin/easy_install[m
[1m+++ b/bin/easy_install[m
[36m@@ -1,4 +1,4 @@[m
[31m-#!/home/a/Projects/todo/bin/python[m
[32m+[m[32m#!/home/s/Projects/melonpage/melonpage/bin/python[m
 # -*- coding: utf-8 -*-[m
 import re[m
 import sys[m
[1mdiff --git a/bin/easy_install-3.9 b/bin/easy_install-3.9[m
[1mindex 27fc112..473e262 100755[m
[1m--- a/bin/easy_install-3.9[m
[1m+++ b/bin/easy_install-3.9[m
[36m@@ -1,4 +1,4 @@[m
[31m-#!/home/a/Projects/todo/bin/python[m
[32m+[m[32m#!/home/s/Projects/melonpage/melonpage/bin/python[m
 # -*- coding: utf-8 -*-[m
 import re[m
 import sys[m
[1mdiff --git a/bin/flask b/bin/flask[m
[1mindex 166881a..2c20c43 100755[m
[1m--- a/bin/flask[m
[1m+++ b/bin/flask[m
[36m@@ -1,4 +1,4 @@[m
[31m-#!/home/a/Projects/todo/bin/python[m
[32m+[m[32m#!/home/s/Projects/melonpage/melonpage/bin/python[m
 # -*- coding: utf-8 -*-[m
 import re[m
 import sys[m
[1mdiff --git a/bin/mako-render b/bin/mako-render[m
[1mindex fd52d73..7ddceb0 100755[m
[1m--- a/bin/mako-render[m
[1m+++ b/bin/mako-render[m
[36m@@ -1,4 +1,4 @@[m
[31m-#!/home/a/Projects/git-todo/melonpage/bin/python[m
[32m+[m[32m#!/home/s/Projects/melonpage/melonpage/bin/python[m
 # -*- coding: utf-8 -*-[m
 import re[m
 import sys[m
[1mdiff --git a/bin/pip b/bin/pip[m
[1mindex 0345274..96b91bf 100755[m
[1m--- a/bin/pip[m
[1m+++ b/bin/pip[m
[36m@@ -1,4 +1,4 @@[m
[31m-#!/home/a/Projects/todo/bin/python[m
[32m+[m[32m#!/home/s/Projects/melonpage/melonpage/bin/python[m
 # -*- coding: utf-8 -*-[m
 import re[m
 import sys[m
[1mdiff --git a/bin/pip-compile b/bin/pip-compile[m
[1mnew file mode 100755[m
[1mindex 0000000..8b2af3f[m
[1m--- /dev/null[m
[1m+++ b/bin/pip-compile[m
[36m@@ -0,0 +1,8 @@[m
[32m+[m[32m#!/home/s/Projects/melonpage/melonpage/bin/python[m
[32m+[m[32m# -*- coding: utf-8 -*-[m
[32m+[m[32mimport re[m
[32m+[m[32mimport sys[m
[32m+[m[32mfrom piptools.scripts.compile import cli[m
[32m+[m[32mif __name__ == '__main__':[m
[32m+[m[32m    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])[m
[32m+[m[32m    sys.exit(cli())[m
[1mdiff --git a/bin/pip-sync b/bin/pip-sync[m
[1mnew file mode 100755[m
[1mindex 0000000..7aea1fb[m
[1m--- /dev/null[m
[1m+++ b/bin/pip-sync[m
[36m@@ -0,0 +1,8 @@[m
[32m+[m[32m#!/home/s/Projects/melonpage/melonpage/bin/python[m
[32m+[m[32m# -*- coding: utf-8 -*-[m
[32m+[m[32mimport re[m
[32m+[m[32mimport sys[m
[32m+[m[32mfrom piptools.scripts.sync import cli[m
[32m+[m[32mif __name__ == '__main__':[m
[32m+[m[32m    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])[m
[32m+[m[32m    sys.exit(cli())[m
[1mdiff --git a/bin/pip3 b/bin/pip3[m
[1mindex 0345274..96b91bf 100755[m
[1m--- a/bin/pip3[m
[1m+++ b/bin/pip3[m
[36m@@ -1,4 +1,4 @@[m
[31m-#!/home/a/Projects/todo/bin/python[m
[32m+[m[32m#!/home/s/Projects/melonpage/melonpage/bin/python[m
 # -*- coding: utf-8 -*-[m
 import re[m
 import sys[m
[1mdiff --git a/bin/pip3.9 b/bin/pip3.9[m
[1mindex 0345274..96b91bf 100755[m
[1m--- a/bin/pip3.9[m
[1m+++ b/bin/pip3.9[m
[36m@@ -1,4 +1,4 @@[m
[31m-#!/home/a/Projects/todo/bin/python[m
[32m+[m[32m#!/home/s/Projects/melonpage/melonpage/bin/python[m
 # -*- coding: utf-8 -*-[m
 import re[m
 import sys[m
[1mdiff --git a/bin/python b/bin/python[m
[1mindex bb60fbf..acd4152 120000[m
[1m--- a/bin/python[m
[1m+++ b/bin/python[m
[36m@@ -1 +1 @@[m
[31m-/home/a/bin/python[m
\ No newline at end of file[m
[32m+[m[32m/usr/bin/python[m
\ No newline at end of file[m
[1mdiff --git a/flasky.py b/flasky.py[m
[1mindex a40c717..c2a7188 100755[m
[1m--- a/flasky.py[m
[1m+++ b/flasky.py[m
[36m@@ -1,13 +1,13 @@[m
 import os [m
 from app import create_app, db[m
[31m-from app.models import Todo, User, Role[m
[32m+[m[32mfrom app.models import Todo, User, Role, Post[m
 from flask_migrate import Migrate[m
 app = create_app(os.getenv("FLASK_CONFIG") or "default")[m
 migrate = Migrate(app, db)[m
 [m
 @app.shell_context_processor[m
 def make_shell_context():[m
[31m-    return dict(db=db, Todo=Todo, User=User, Role=Role)[m
[32m+[m[32m    return dict(db=db, Todo=Todo, User=User, Role=Role, Post=Post)[m
 [m
 @app.cli.command()[m
 def test():[m
[1mdiff --git a/include/site/python3.9/greenlet/greenlet.h b/include/site/python3.9/greenlet/greenlet.h[m
[1mold mode 100755[m
[1mnew mode 100644[m
[1mdiff --git a/migrations/versions/e84c74bdf302_.py b/migrations/versions/e84c74bdf302_.py[m
[1mnew file mode 100644[m
[1mindex 0000000..35ceb18[m
[1m--- /dev/null[m
[1m+++ b/migrations/versions/e84c74bdf302_.py[m
[36m@@ -0,0 +1,71 @@[m
[32m+[m[32m"""empty message[m
[32m+[m
[32m+[m[32mRevision ID: e84c74bdf302[m
[32m+[m[32mRevises: 3fce30597c90[m
[32m+[m[32mCreate Date: 2021-05-16 09:32:40.497649[m
[32m+[m
[32m+[m[32m"""[m
[32m+[m[32mfrom alembic import op[m
[32m+[m[32mimport sqlalchemy as sa[m
[32m+[m
[32m+[m
[32m+[m[32m# revision identifiers, used by Alembic.[m
[32m+[m[32mrevision = 'e84c74bdf302'[m
[32m+[m[32mdown_revision = '3fce30597c90'[m
[32m+[m[32mbranch_labels = None[m
[32m+[m[32mdepends_on = None[m
[32m+[m
[32m+[m
[32m+[m[32mdef upgrade():[m
[32m+[m[32m    # ### commands auto generated by Alembic - please adjust! ###[m
[32m+[m[32m    op.create_table('users',[m
[32m+[m[32m    sa.Column('id', sa.Integer(), nullable=False),[m
[32m+[m[32m    sa.Column('username', sa.String(length=128), nullable=True),[m
[32m+[m[32m    sa.Column('email', sa.String(length=128), nullable=True),[m
[32m+[m[32m    sa.Column('role_id', sa.Integer(), nullable=True),[m
[32m+[m[32m    sa.Column('password_hash', sa.String(length=128), nullable=True),[m
[32m+[m[32m    sa.Column('confirmed', sa.Boolean(), nullable=True),[m
[32m+[m[32m    sa.Column('member_since', sa.DateTime(), nullable=True),[m
[32m+[m[32m    sa.Column('about_me', sa.Text(), nullable=True),[m
[32m+[m[32m    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),[m
[32m+[m[32m    sa.PrimaryKeyConstraint('id')[m
[32m+[m[32m    )[m
[32m+[m[32m    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)[m
[32m+[m[32m    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)[m
[32m+[m[32m    op.create_table('posts',[m
[32m+[m[32m    sa.Column('id', sa.Integer(), nullable=False),[m
[32m+[m[32m    sa.Column('body', sa.Text(), nullable=True),[m
[32m+[m[32m    sa.Column('timestamp', sa.DateTime(), nullable=True),[m
[32m+[m[32m    sa.Column('author_id', sa.Integer(), nullable=True),[m
[32m+[m[32m    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),[m
[32m+[m[32m    sa.PrimaryKeyConstraint('id')[m
[32m+[m[32m    )[m
[32m+[m[32m    op.create_index(op.f('ix_posts_timestamp'), 'posts', ['timestamp'], unique=False)[m
[32m+[m[32m    op.drop_index('ix_user_email', table_name='user')[m
[32m+[m[32m    op.drop_index('ix_user_username', table_name='user')[m
[32m+[m[32m    op.drop_table('user')[m
[32m+[m[32m    # ### end Alembic commands ###[m
[32m+[m
[32m+[m
[32m+[m[32mdef downgrade():[m
[32m+[m[32m    # ### commands auto generated by Alembic - please adjust! ###[m
[32m+[m[32m    op.create_table('user',[m
[32m+[m[32m    sa.Column('id', sa.INTEGER(), nullable=False),[m
[32m+[m[32m    sa.Column('username', sa.VARCHAR(length=128), nullable=True),[m
[32m+[m[32m    sa.Column('email', sa.VARCHAR(length=128), nullable=True),[m
[32m+[m[32m    sa.Column('role_id', sa.INTEGER(), nullable=True),[m
[32m+[m[32m    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),[m
[32m+[m[32m    sa.Column('confirmed', sa.BOOLEAN(), nullable=True),[m
[32m+[m[32m    sa.Column('about_me', sa.TEXT(), nullable=True),[m
[32m+[m[32m    sa.Column('member_since', sa.DATETIME(), nullable=True),[m
[32m+[m[32m    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),[m
[32m+[m[32m    sa.PrimaryKeyConstraint('id')[m
[32m+[m[32m    )[m
[32m+[m[32m    op.create_index('ix_user_username', 'user', ['username'], unique=1)[m
[32m+[m[32m    op.create_index('ix_user_email', 'user', ['email'], unique=1)[m
[32m+[m[32m    op.drop_index(op.f('ix_posts_timestamp'), table_name='posts')[m
[32m+[m[32m    op.drop_table('posts')[m
[32m+[m[32m    op.drop_index(op.f('ix_users_username'), table_name='users')[m
[32m+[m[32m    op.drop_index(op.f('ix_users_email'), table_name='users')[m
[32m+[m[32m    op.drop_table('users')[m
[32m+[m[32m    # ### end Alembic commands ###[m
[1mdiff --git a/pyvenv.cfg b/pyvenv.cfg[m
[1mindex 3448a29..5c102c1 100755[m
[1m--- a/pyvenv.cfg[m
[1m+++ b/pyvenv.cfg[m
[36m@@ -1,3 +1,3 @@[m
[31m-home = /home/a/bin[m
[32m+[m[32mhome = /usr/bin[m
 include-system-site-packages = false[m
 version = 3.9.2[m
[1mdiff --git a/testing.db b/testing.db[m
[1mindex 2940165..96812ad 100644[m
Binary files a/testing.db and b/testing.db differ
