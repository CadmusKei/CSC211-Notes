# Uploading a Project to GitHub via CLI

As Computer Scientists it is very important to upload our work to GitHub.

GitHub is vital to us in many ways. It:

- Provides a space to backup our code
- Provides a space to collaborate.
- Provides version control (perhaps you want to test different versions of your project, we can use branches).
- Works as a portfolio to share and show your work to peers and employers. (Subtle Plug: [https://github.com/CadmusKei](https://github.com/CadmusKei))
- Provides a space for hosting projects such as personal websites or serverless webapps.

As you can see, it’s a very powerful tool.

---

## GitHub Terminology

- A space on GitHub showcasing or storing your project is called a _repository_ or _repo_.
- When we upload to GitHub we call it _pushing_ to the repo.
- When we have done some changes or updates to our project, we describe them before we push, this is called a _commit_.
- When we have many versions of our projects, we call each version a _branch._ (Think branches of a tree).

---

# Uploading to GitHub

There are many ways to push your work to GitHub. A crucial one that all Computer Scientists should understand is via the CLI (Command Line Interface). This is when we commit via the terminal.

![image.png](attachment:f33b5bbb-685c-459b-a5f2-d086cef96f8b:image.png)

Some other versions worth mentioning are:

- Via the GitHub website GUI.
- Via most modern IDEs (requires a little set-up but becomes incredibly convenient).

---

# CLI Method

> NB: Before starting, make sure you have Git installed.

You can check if you have git installed by running:

```bash
git --version
```

in the terminal. Otherwise install git here: [https://git-scm.com/install/](https://git-scm.com/install/)

### Step 1: Navigate

You can open your terminal by searching `cmd` on your machine.

The first step to uploading your work to a repository is to navigate to it via the terminal.

![image.png](attachment:be6b4c02-50b4-4ef2-860a-494e1571f5cf:image.png)

Once here you can navigate by writing `cd` which is the command for “Go To” and then pasting the directory to your project.

```java
cd path/to/your/project
```

You can quickly access your path by clicking “File → Open” in your IDE and copying the path in the explorer.

![image.png](attachment:733f1876-fbd6-4395-8cd8-d0d65a156bad:image.png)

### Step 2: Initialise

Initialise git in the folder

```java
git init
```

### Step 3: Add

Add everything in the folder to git. (Tell git what you should upload)

In this example the `.` (fullstop) means “everything”

```bash
git add .
```

Alternatively if you just want to add one file or folder you can type

```bash
git add example.png
```

### Step 4: Commit

Commit the files, and create a “snapshot” of the upload.

```bash
git commit -m "Initial commit"
```

### Step 5: Create the repo on Github

Go to the GitHub website at [https://github.com/](https://github.com/) and create a new repo. Copy the URL to the repo when you have created it and are in it.

![image.png](attachment:ac3aaf9e-8a9d-41cf-82d7-2f3839062be3:image.png)

eg:

```bash
<https://github.com/username/my-project.git>
```

### Step 6: Connect your local repo to the GitHub repo

```bash
git remote add origin <https://github.com/username/my-project.git>
```

This “clones” the repo.

### Step 7: Push to Github

```bash
git branch -M main
git push -u origin main
```

At this step, if it is your first time, you may be asked to connect to your GitHub, there are a few ways but each of them are simple and you will be guided through them by GitHub.

### After first upload

After your first upload you will have way less steps and your workflow will be centered around adding, committing and pushing.

```bash
git add .
git commit -m "Describe your changes"
git push
```

### Summary of steps first time

```bash
cd project-folder
git init
git add .
git commit -m "Initial commit"
git remote add origin <https://github.com/username/repo.git>
git branch -M main
git push -u origin main
```

## Flex your dedication!

GitHub provides a little data on your commits throughout the years, programmers like to use this to track their _commit_ment and flex!