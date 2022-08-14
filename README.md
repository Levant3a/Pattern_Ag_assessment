# Pattern_Ag_assessment
Git repository for the Pattern Ag assessment

I have stored a yml file in the scripts directory that would generate the conda environment I used to run this assessment.

To create the conda environment please use this command in the command line:

conda env create -f environment.yml

For more information on conda environments here is a link. https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

To run my assessment you would just need to write this command:

python assessment_process.py

assessment_process.py is basically a wrapper script that will run through the rest of the tasks. 

What is good about this is that you can eventually add in breakers to selectively use whichever task you want from an overall script.

Then in the future make a command line script that can run it on its own once a month or once a year.

assessment_process.py will call in these following scripts task_1.py, task_2.py, task_3.py, task_4.py

Notes: 
I went a little to long on the exploration and set up I could not completely finish task_4.py 

I just started trying to parse through the crops field_geometry column and tried to get the center of the string for each row.

That would have allowed me to get the lat and lon for the lookup to the provided url for the fips_code mapping

Task 3 I was confused on the calculation so I just assumed how it would be done

 comppct * col * hlw /100 for col in om, cec, ph

If given more time I would have liked to complete task_4 and done more cleanup.