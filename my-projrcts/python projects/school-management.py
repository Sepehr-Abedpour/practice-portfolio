import mariadb

# etesal be db 

try :
    connection = mariadb.connect(
        host = 'localhost',
        user = 'root' ,
        password = 'Sepehr007',
        database = 'students'
    )
    cursor = connection.cursor()
    print('database connected successfully !')
except mariadb.Error as error :
    print('database connection failed!')
    print(error)
    exit()
    
# ezafe kardan daneshamooz

def add_student() :
    print('\n==========ADD STUDENT==========')
    id = int(input('enter id :'))
    name = input('enter estudent name :')
    age = int(input('enter student age :'))
    height = float(input('enter height :'))
    
    cursor.execute(
        """
        INSERT INTO students (id,name,age,height)
        VALUES (?,?,?,?)
        """,
        (id,name,age,height)
    )
    connection.commit()
    print('\n student added successfully !')
    
#neshan dadan tamam danesh amoozan

def show_student() :
    print('\n==========ALL STUDENT==========')
    cursor.execute(
        """
        SELECT id,name ,age ,height FROM students
        """
    )
    students = cursor.fetchall()
    if not students :
        print('there are no students.')
        return
    print('\nid|name|age|height')
    print('-'*35)
    for student in students :
        print(
            f'{student[0]}|'
            f'{student[1]}|'
            f'{student[2]}|'
            f'{student[3]}'
        )
        
# jostojou yek daneshamooz

def search_student() :
    print('\n==========SEARCH STUDENT==========')
    student_id = int(input('enter student id:'))
    cursor.execute(
        """
        SELECT id,name,age,height FROM students
        WHERE id = ?
        """,
        (student_id,)
    )
    student = cursor.fetchone()
    if student :
        print('\nStudnet found!')
        print('id:' , student[0])
        print('name:', student[1])
        print('age:', student[2])
        print('height:',student[3])
    else :
        print('\nStudent not found!')
        
# taghyire etelaat

def update_student() : 
    print('\n==========UPDATE STUDENT==========')
    student_id = int(input('enter student id:'))
    cursor.execute(
        """
        SELECT id FROM students 
        WHERE id = ?
        """,
        (student_id,)
    )
    student = cursor.fetchone()
    if not student :
        print ('\nStudent not found !')
        return
    
    new_name = input('enter new name :')
    new_age = int(input('enter new age :'))
    new_height = float(input('enter new height :'))
    
    cursor.execute(
        """
        UPDATE students
        SET name = ?,
            age = ?,
            height = ?
        WHERE id = ?
        """,
        (new_name,
         new_age,
         new_height,
         student_id
        )
    )
    connection.commit()
    print('\nstudent update successfully !')
    
# hazf daneshamooz 

def delete_student() : 
    print('\n==========DELETE STUDENT==========')
    student_id = int(input('enter student id :'))
    cursor.execute(
        """
        SELECT name FROM students 
        WHERE id = ?
        """,
        (student_id,)
    )
    student = cursor.fetchone()
    if not student :
        print('\nstudent not found !')
        return
    print (f'\nstudent : {student[0]}')
    confirmation = input('are you sure you want to delete this student ?(y/n):')
    if confirmation.lower() == 'y' :
        cursor.execute(
            """
            DELETE FROM students 
            WHERE id = ?
            """,
            (student_id)
        )
        connection.commit()
        print('\nStudent delete successfully !')
    else :
        print('\ndelete cancelled.')
        
# mohasebat amar class 

def class_statistics() :
    print('\n==========CLASS STATISTICS==========')
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM students
        """
    )
    student_count = cursor.fetchone()[0]
    if student_count == 0:
        print('there are no students.')
        return
    
# average sen
    cursor.execute(
        """
        SELECT AVG(age)
        FROM students
        """
    )
    average_age = cursor.fetchone()[0]
    
# average ghad
    cursor.execute(
        """
        SELECT AVG(height)
        FROM students
        """
    )
    average_height = cursor.fetchone()[0]
    
# bishtarin ghad
    cursor.execute(
          """
          SELECT MAX(height)
          FROM students
          """
      )
    max_height = cursor.fetchone()[0]
    
# kamtarin ghad 
    cursor.execute(
        """
          SELECT MIN(height)
          FROM students
          """
      )
    min_height = cursor.fetchone()[0] 
    
    print(f'\nnumber of students : {student_count}')
    print(f'average age : {average_age}')
    print(f'average height : {average_height}')
    print(f'max height : {max_height}')
    print(f'min height : {min_height}')
    
# MAIN MENU
while True :
    print('\n')
    print('=' * 40 )
    print('      SCHOOL MANAGEMENT SYSTEM      ')
    print('=' * 40 )  
    print('1. add student')
    print('2. show all student')
    print('3. search student')
    print('4. update student')
    print('5. delete student')
    print('6. class statistics')
    print('7. exit')
    print('=' * 40 )
    
    choice = input('choose an option :')
    if choice == '1' :
        add_student()
    elif choice == '2' :
        show_student()
    elif choice == '3' :
        search_student()
    elif choice == '4' :
        update_student()
    elif choice == '5' :
        delete_student()
    elif choice == '6' :
        class_statistics()
    elif choice == '7' :
        print('\nGoodbye')
        break
    else :
        print('\nInvalid choice!')
        
# bastan connection

cursor.close()
connection.close()
print('database connection closed.')

        
           