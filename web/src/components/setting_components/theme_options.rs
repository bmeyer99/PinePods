use yew::prelude::*;

#[function_component(ThemeOptions)]
pub fn theme() -> Html {
    html! {
        <div class="p-4"> // You can adjust the padding as needed
            <p class="text-lg font-bold mb-4">{"Select Theme"}</p> // Styled paragraph

            <div class="relative inline-block text-gray-700">
                <select class="appearance-none w-full bg-white border border-gray-300 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline">
                    <option>{"Option 1"}</option>
                    <option>{"Option 2"}</option>
                    <option>{"Option 3"}</option>
                </select>
                <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M6.293 9.293a1 1 0 0 1 1.414 0L10 10.586l2.293-2.293a1 1 0 1 1 1.414 1.414l-3 3a1 1 0 0 1-1.414 0l-3-3a1 1 0 0 1 0-1.414z"/></svg>
                </div>
            </div>

            <button class="mt-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button">
                {"Submit"}
            </button>
        </div>
    }
}
