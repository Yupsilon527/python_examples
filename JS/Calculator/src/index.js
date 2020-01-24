import React from "react";
import ReactDOM from "react-dom";

import "./styles.css";

class CalculatorDisplay extends React.Component {
  render() {
    return (
      <div className="Screen">
        <h2>{this.props.old_value}</h2>
        <h1>{this.props.new_value}</h1>
      </div>
    );
  }
}

class Calculator extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      old_value: "",
      new_value: "",
      cleared: false
    };
  }

  renderButton(i) {
    var buttonValues = [
      "1",
      "2",
      "3",
      "+",
      "4",
      "5",
      "6",
      "-",
      "7",
      "8",
      "9",
      "/",
      "<",
      "0",
      "=",
      "*"
    ];

    return (
      <button onClick={() => this.handleButton(i)}>{buttonValues[i]}</button>
    );
  }
  expandNewValue(value) {
    if (this.state.cleared) {
      this.setState({ old_value: "" });
      this.setState({ cleared: false });
    }
    this.setState({ new_value: this.state.new_value + value });
  }
  expandOldValue(value, sign) {
    if (value !== "") {
      if (this.state.old_value !== "") {
        var oldcalc = this.state.old_value;
        var oldsign = oldcalc[oldcalc.length - 1];

        var numberA = parseFloat(oldcalc.substring(0, oldcalc.length - 1));
        var numberB = parseFloat(value);

        switch (oldsign) {
          case "+":
            value = numberA + numberB;
            break;
          case "-":
            value = numberA - numberB;
            break;
          case "*":
            value = numberA * numberB;
            break;
          case "/":
            value = numberA / numberB;
            break;

          default:
            break;
        }
      }
      if (sign !== "=") {
        this.setState({ old_value: value + sign });
      } else {
        this.setState({ old_value: value });
        this.setState({ cleared: true });
      }
      this.setState({ new_value: "" });
    }
  }
  handleButton(i) {
    switch (i) {
      default:
        this.expandOldValue(this.state.new_value, "=");
        break;
      case 0: // 1
        this.expandNewValue("1");
        break;
      case 1: // 2
        this.expandNewValue("2");
        break;
      case 2: // 3
        this.expandNewValue("3");
        break;
      case 3: // +
        this.expandOldValue(this.state.new_value, "+");
        break;
      case 4: // 4
        this.expandNewValue("4");
        break;
      case 5: // 5
        this.expandNewValue("5");
        break;
      case 6: // 6
        this.expandNewValue("6");
        break;
      case 7: // -
        this.expandOldValue(this.state.new_value, "-");
        break;
      case 8: // 7
        this.expandNewValue("7");
        break;
      case 9: // 8
        this.expandNewValue("8");
        break;
      case 10: // 9
        this.expandNewValue("9");
        break;
      case 11: // /
        this.expandOldValue(this.state.new_value, "/");
        break;
      case 12: // <
        var name = this.state.new_value;
        this.setState({ new_value: name.substring(0, name.length - 1) });
        break;
      case 13: // 0
        this.expandNewValue("0");
        break;
      case 15: // *
        this.expandOldValue(this.state.new_value, "*");
        break;
    }
  }

  render() {
    return (
      <div className="App">
        <CalculatorDisplay
          old_value={this.state.old_value}
          new_value={this.state.new_value}
        />
        <div className="btn-row">
          {this.renderButton(0)}
          {this.renderButton(1)}
          {this.renderButton(2)}
          {this.renderButton(3)}
        </div>
        <div className="btn-row">
          {this.renderButton(4)}
          {this.renderButton(5)}
          {this.renderButton(6)}
          {this.renderButton(7)}
        </div>
        <div className="btn-row">
          {this.renderButton(8)}
          {this.renderButton(9)}
          {this.renderButton(10)}
          {this.renderButton(11)}
        </div>
        <div className="btn-row">
          {this.renderButton(12)}
          {this.renderButton(13)}
          {this.renderButton(14)}
          {this.renderButton(15)}
        </div>
      </div>
    );
  }
}

const rootElement = document.getElementById("root");
ReactDOM.render(<Calculator />, rootElement);
