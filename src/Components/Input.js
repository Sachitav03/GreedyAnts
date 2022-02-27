import React from 'react';
import { useState } from "react";
import axios from "axios";


let ingredient_list = ""


function Input(props){
    const [query, setQuery] = useState("");


    const handleSubmit = (event) => {
        event.preventDefault()
        ingredient_list = query
        //alert(ingredient_list)
        postData(ingredient_list);
    }


    function postData(ingredient_list) {
        axios({
          method: "GET",
          url:"https://fecb-169-234-5-222.ngrok.io/?ingr=" + ingredient_list,
        })
        .then((response) => {
          console.log(response.data)
          props.setRecipeDataa(response.data)
        }).catch((error) => {
          if (error.response) {
            console.log(error.response)
            console.log(error.response.status)
            console.log(error.response.headers)
            }
        })}

    return (
        <form onSubmit = {handleSubmit}>
        <input placeholder = "Enter Ingredients"
            type="text"
            name=""
            value={query}
            onChange={(e) => setQuery(e.target.value)}
        />
        </form>
    )
}

export default Input;
//event => setQuery(event.target.value)