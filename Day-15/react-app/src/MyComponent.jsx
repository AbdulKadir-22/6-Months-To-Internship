import React,{ useState } from 'react';

function MyComponent(){

    const [intro,setIntro] = useState([]);
    const [name,setName] = useState("");
    const [course, setCourse] = useState("");
    const [year, setYear] = useState(new Date().getFullYear());

    function handleAddIntro(){

        const newStudent = {name : name,
                         course: course,
                         year: year};

        setIntro(prevIntro => [...prevIntro, newStudent])

    }

    function handleRemoveIntro(index){
            setIntro(prevIntro => prevIntro.filter((_, i) => i !== index));
    }

    function handleNameChange(event){
        setName(event.target.value);
    }

    function handleCourseChange(event){
        setCourse(event.target.value);
    }

    function handleYearChange(event){
        setYear(event.target.value);
    }

    return (<div>
        <h2>Student Intro</h2>
        <ul>
            {intro.map((student, index) => (
                <li key={index} onClick={() => handleRemoveIntro(index)}>
                    {student.name} - {student.course} - {student.year}
                </li>
            ))}
        </ul>
            <input type="text" value={name} onChange={handleNameChange} placeholder='Enter Your Name'/>
            <br/><br/>
            <input type="text" value={course} onChange={handleCourseChange} placeholder='Enter Your Course'/>
            <br/><br/>
            <input type="number" value={year} onChange={handleYearChange} placeholder='Enter Your Admission Year'/>
            <br/><br/>
            <button onClick={handleAddIntro}>Add Intro ➕ </button>

    </div>)


}

export default MyComponent;