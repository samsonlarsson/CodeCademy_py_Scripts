var canIWatch = function (age) 
{
	if (age >= 1 && age <= 5) {
		 return "You are not allowed to watch Deadpool after 6.00pm.";
	} else if (age >= 6 && age <= 16) {
		return "You must be accompanied by a guardian who is 21 or older.";
	} else if (age >= 17 && age <= 24) {
		return "You are allowed to watch Deadpool, right after you show some ID.";
	} else if (age > 25) {
		return "Yay! You can watch Deadpool with no strings attached!";
	} else {
		return "Invalid age.";
	}
}
