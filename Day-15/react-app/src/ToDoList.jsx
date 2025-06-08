import React, { useState} from 'react';

function ToDoList(){
    const [task, setTask] = useState([]);
    const [newTask, setNewTask] = useState("");

    function handleInputChange(event){
        setNewTask(event.target.value)
    }

    function addTask(){
        if(newTask.trim() !== ""){
            setTask(prevtask => [...prevtask,newTask])
            setNewTask("")
        }

    }
    function removeTask(index){
        const updatedTask = task.filter((_,i) => i !== index);
        setTask(updatedTask)
    }

    return(
        <>
            <div className='To-Do-List'>
                <h1>To-Do-list</h1>
                <div>
                    <input  type='text' 
                            value={newTask} 
                            placeholder='Enter New Task...' 
                            onChange={handleInputChange}/>
                    <button onClick={addTask}>Add➕</button>
                </div>
                <ol>
                    {task.map((task,index) => 
                     <li key={index}>
                         <span>{task}</span>
                         <span className='delete-button' onClick={() => removeTask(index)}>Delete</span>
                     </li>
                    )}
                </ol>
            </div>
        </>
    );
}

export default ToDoList;