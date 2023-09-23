# GITLY - Gitlab User Retriver

A user-friendly interface for interacting with the [Gitlab](https://about.gitlab.com/) API endpoint containing users data and managing the retrieved data in a quick and simple manner.

[![Watch the video](https://img.youtube.com/vi/9SN4rfi94pk/maxresdefault.jpg)](https://youtu.be/9SN4rfi94pk)

## USAGE:

- Download tool (Options - Direct download /git clone):

```markdown
    git clone https://github.com/stevemats/Gitly.git
```

- Change directory to Gitly(path to Gitly download):

```markdown
cd Gitly
```

- Running the Gitly(run below command and follow prompt):

```markdown
python gitly.py
```

- By default data is stores in `user_data.txt` file but you can save it somewhere else.

## Prompt Screenshot

---

![gitly options gitlab](https://github.com/stevemats/Gitly/assets/30528167/d16d0355-d17f-4db6-967a-dcd29eb2cbef)

- **Enter the number of results per page** = This prompt allows you to specify how many results(user records) you want to receive on each page.

- **Enter the username to search for** = Input the username you're interested in searching for within the API's user data so as to filter and retrieve specific user information.

- **Enter the total number of pages to retrieve (0 for all)** = This prompt provides an option to limit the number of pages of data you want to retrieve. If you enter a number >0, the script will fetch that amount of pages which can be helpful if you only want to retrieve a specific portion of the data. If you enter "0", it will retrieve all available pages of data.

- **Enter the output file name** This gives you the ability to define how the output data will be saved which can be very handy if you want to seperate user data by name.
