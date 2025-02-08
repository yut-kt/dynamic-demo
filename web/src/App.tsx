import React, {lazy} from 'react';
import './App.css';

const PatternA = lazy(() =>
    import('./components/PatternA.tsx')
);

const PatternB = lazy(() =>
    import('./components/PatternB.tsx')
);

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {process.env.REACT_APP_PATTERN === 'A' ? <PatternA /> : <PatternB />}
      </header>
    </div>
  );
}

export default App;
