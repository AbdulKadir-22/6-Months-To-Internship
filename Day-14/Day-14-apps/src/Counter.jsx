import React, {useState} from 'react';

function Counter(){
    const [count, setCount] = useState(0);

    const increment = () =>{
        setCount(count + 1);
    } 
    const decrement = () =>{
        setCount(count - 1);
    } 
    const reset = () =>{
        setCount(0);
    } 

    return(
        <div className='container'>
            <p id="count">{count}</p>
            <button  className ="counter" onClick={decrement}>Decrement</button>
            <button  className ="counter" onClick={reset}>reset</button>
            <button  className ="counter" onClick={increment}>increment</button>
        </div>
    )
}

export default Counter