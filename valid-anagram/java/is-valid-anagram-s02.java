public static boolean isAnagram(String s, String t) {
        String sortS = s.chars().sorted().collect(
                StringBuilder::new,
                StringBuilder::appendCodePoint,
                StringBuilder::append
        ).toString();

        String sortT = t.chars().sorted().collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append).toString();

        return sortS.equals(sortT);
    }