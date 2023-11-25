import './App.css'
import Transliterator from "./components/Transliterator.jsx";
import UTFHandler from "./components/UTFHandler.jsx";
import ChatComponent from "./components/ChatComponent.jsx";

function App() {
  return (
      <>
        <div>
            <Transliterator/>
            <UTFHandler/>
            <ChatComponent/>
        </div>
      </>
  )
}

export default App
