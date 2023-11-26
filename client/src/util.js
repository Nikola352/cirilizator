export function convertUnicodeToString(unicodeString) {
    // Remove null characters and split the string into an array
    var stringArray = unicodeString.split('\u0000');

    // Remove empty strings from the array
    var filteredArray = stringArray.filter(function (element) {
        return element !== '';
    });

    // Join the array elements into a normal string
    var normalString = filteredArray.join('');

    return normalString;
}