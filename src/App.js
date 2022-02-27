import './App.css';
import { useState, createContext } from 'react'
import axios from "axios";

import Title from './Components/Title.js';
import Input from './Components/Input.js';
import About from './Components/About.js';
import RecipeList from './Components/RecipeList.js';

import keep from "./keep.png";
import banana from "./banana.jpg";


function App() {

  const [recipeDataa, setRecipeDataa] = useState([])

  function getData() {
    axios({
      method: "GET",
      url:"/",
    })
    .then((response) => {
      console.log(response.data)
      const res =response.data
      setRecipeDataa(({
        recipe_name: res.name,
        recipe_image: res.image,
        recipe_ingredients: res.ingredients,
        recipe_instructions: res.instructions,
        }))
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}

  return (
    <div className="App">
      <header className="App-header">

        <div className="split left">
          
        <div className="">
            <img src={keep} alt="Logo"/>
        </div>
        <div className="centeredLeft">
          <Title/>
            
          <Input handleSubmit={(e) => getData()} setRecipeDataa={setRecipeDataa}/>
          <About />
          </div>

        </div>

        <div className="split right">
          <div className="centeredRight">
            <div className="recipeTitle">
            </div>
            <div className="chicken">
            

            {recipeDataa.length!=0 &&
            <div>
              <h1>{recipeDataa[0]['0']}</h1>
              <img src={recipeDataa[0]['1']}/>
              <h4>Ingredients:</h4>
              <p>{recipeDataa[0]['2']}</p>
              <h4>Instructions:</h4>
              <p>{recipeDataa[0]['3']}</p>
            </div>
            }
            </div>
              
              {/* {recipeDataa.map(rexs => (
                <> 
                <h1>{rexs["0"]}</h1>
                <img src={rexs['1']}/>
                </>
              ))} */}
            </div>
        </div>

        
          
        
      </header>
    </div>

  );
}

export default App;
