// import Recipe from './Components/Recipe.js';


function Recipe(props){
    return <>
        <p> {props.name} </p> 
        <img src={props.image}/>
        <p> {props.ingredients} </p>
        <p> {props.instructions} </p>
        </>
}


function RecipeList() {
    return(<>
        <h2>Recipes</h2>
        <Recipe name=""/>
        <Recipe image=""/>
        <Recipe ingredients=""/>
        <Recipe instructions=""/>
    </>);
}

export default RecipeList