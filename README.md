https://helpdeskgpa.pythonanywhere.com/


Steps to execute CUDA program
On your CPU(host) open terminal
1. Login to the server i.e GPU by executing the following command

ssh 172.16.8.97

2. It will prompt you for password (Enter password)
3. Create a empty file through terminal using following command

`touch file_name.cu`

4. To open the file write the following command in the terminal

`vim file_name.cu`

5. i) Press ‘i’ to get into the inserting mode.
ii) After completion of the code press ‘ESC’ to exit inserting mode
6. To save and exit the file press :wq
7. To run the file create an object file by using following command

‘ nvcc file_name.cu -o obj_name’
8. To execute the object file use the command

‘ ./obj_name‘
