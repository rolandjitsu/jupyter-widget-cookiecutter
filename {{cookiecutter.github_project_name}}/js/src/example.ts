// tslint:disable: max-classes-per-file
import {DOMWidgetModel, DOMWidgetView} from 'jupyter-js-widgets';


const name = '{{ cookiecutter.npm_package_name }}';
const version = '{{ cookiecutter.npm_package_version }}';


/**
 * Custom Model
 *
 * Custom widgets models must at least provide default values for model attributes,
 * when different from the base class,
 * including: {_view_name, _view_module, _view_module_version, _model_name, _model_module, _model_module_version}.
 *
 * NOTE: When serialiazing the entire widget state for embedding,
 * only values that differ from the defaults will be specified.
 */

export class HelloModel extends DOMWidgetModel {
	defaults() {
		return {
			...super.defaults(),
			_model_name: 'HelloModel',
			_view_name: 'HelloView',
			_model_module: name,
			_view_module: name,
			_model_module_version: version,
			_view_module_version: version,
			value: 'Hello World :)'
		};
	}
}


/**
 * Custom View
 * Renders the widget model.
 */
export class HelloView extends DOMWidgetView {
	render() {
		// Bind model listeners
		this.model.on('change:value', this.updateText, this);
		// Trigger initial model change
		this.updateText();
	}

	private updateText() {
		this.el.textContent = this.model.get('value');
	}
}
