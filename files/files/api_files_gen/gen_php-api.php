#!/usr/bin/env php
<?php
/* Instructions:
Download PHP Manual: git clone https://github.com/php/doc-en
Run this script from doc-en/reference/:
- no parameters: Generate Core, Bundled and External extensions (https://php.net/extensions.membership)
- parameter "all": Generate all extensions
- other parameters, e.g. "imap mysql oci8 pdo_oci pdo_sqlsrv sqlsrv": Generate Core, Bundled, External and the ones provided
Translations: Put doc-es alongside doc-en and run from doc-es/reference/.
*/

const SEP = "\t"; // calltip.hypertext.end.definition

$dirs = array("../language/predefined");
array_shift($argv);
$enReference = "../../doc-en/reference/";
if ($argv == array("all")) {
	foreach (glob("$enReference*") as $dir) {
		$dirs[] = substr($dir, strlen($enReference));
	}
	$dirs = glob("*", GLOB_ONLYDIR);
} else {
	$xml = simplexml("../../doc-en/appendices/extensions.xml");
	foreach ($xml->xpath("//section") as $section) {
		if (preg_match('~^extensions\.membership\.(core|bundled|external)$~', $section["id"])) {
			foreach ($section->itemizedlist->listitem as $listitem) {
				$dirs[] = preg_replace('~^(book|ref)\.~', '', str_replace("-", "_", $listitem->para->xref["linkend"]));
			}
		}
	}
	$dirs = array_merge($dirs, $argv);
}

/* Structure of php.api:
self parent $this
https://php.net/reserved.variables
https://php.net/reserved.keywords without functions()
https://php.net/reserved.constants without E_, __COMPILER_HALT_OFFSET__, true, false, null
https://php.net/reserved.other-reserved-words
https://php.net/language.oop5.magic
extensions functions and classes
extensions constants
*/
file_put_contents("php.api", str_replace(" ", "\n", 'self parent $this'
	. ' $GLOBALS $_SERVER $_GET $_POST $_FILES $_REQUEST $_SESSION $_ENV $_COOKIE $php_errormsg $http_response_header $argc $argv'
	. ' abstract and as break callable case catch class clone const continue declare default do echo else elseif enddeclare endfor endforeach endif endswitch endwhile extends final finally fn for foreach function global goto if implements include include_once instanceof insteadof interface match namespace new or print private protected public readonly require require_once return static switch throw trait try use var while xor yield from'
	. ' __CLASS__ __DIR__ __FILE__ __FUNCTION__ __LINE__ __METHOD__ __PROPERTY__ __NAMESPACE__ __TRAIT__'
	. ' PHP_VERSION PHP_MAJOR_VERSION PHP_MINOR_VERSION PHP_RELEASE_VERSION PHP_VERSION_ID PHP_EXTRA_VERSION ZEND_THREAD_SAFE ZEND_DEBUG_BUILD PHP_ZTS PHP_DEBUG DEBUG_BACKTRACE_PROVIDE_OBJECT DEBUG_BACKTRACE_IGNORE_ARGS PHP_MAXPATHLEN PHP_OS PHP_OS_FAMILY PHP_SAPI PHP_EOL PHP_INT_MAX PHP_INT_MIN PHP_INT_SIZE PHP_FLOAT_DIG PHP_FLOAT_EPSILON PHP_FLOAT_MIN PHP_FLOAT_MAX DEFAULT_INCLUDE_PATH PHP_PREFIX PHP_BINDIR PHP_SBINDIR PHP_BINARY PHP_MANDIR PHP_LIBDIR PHP_DATADIR PHP_SYSCONFDIR PHP_LOCALSTATEDIR PHP_CONFIG_FILE_PATH PHP_CONFIG_FILE_SCAN_DIR PHP_SHLIB_SUFFIX PHP_FD_SETSIZE PHP_WINDOWS_EVENT_CTRL_C PHP_WINDOWS_EVENT_CTRL_BREAK PHP_CLI_PROCESS_TITLE STDERR STDIN STDOUT'
	. ' int float bool string true false null void iterable object mixed never enum resource numeric') . '
__construct(mixed ...$values)' . SEP . 'Object constructor
__destruct()' . SEP . 'Object destructor
__call(string $name, array $arguments): mixed' . SEP . 'Triggered when invoking inaccessible methods in an object context
__callStatic(string $name, array $arguments): mixed' . SEP . 'Triggered when invoking inaccessible methods in a static context
__get(string $name): mixed' . SEP . 'Utilized for reading data from inaccessible properties
__set(string $name, mixed $value): void' . SEP . 'Run when writing data to inaccessible properties
__isset(string $name): bool' . SEP . 'Triggered by calling isset() or empty() on inaccessible properties
__unset(string $name): void' . SEP . 'Invoked when unset() is used on inaccessible properties
__sleep(): array' . SEP . 'Called by serialize()
__wakeup(): void' . SEP . 'Called by unserialize()
__serialize(): array' . SEP . 'Called by serialize()
__unserialize(array $data): void' . SEP . 'Called by unserialize()
__toString(): string' . SEP . 'Decide how to react when object is converted to a string
__invoke(mixed ...$values): mixed' . SEP . 'Called when a script tries to call an object as a function
__set_state(array $properties): object' . SEP . 'Called by var_export() result
__clone(): void' . SEP . 'Called after cloning
__debugInfo(): array' . SEP . 'Called by var_dump()
');

foreach ($dirs as $dir) {
	echo ".";
	
	$translations = array();
	if (basename(dirname(dirname(realpath($dir)))) != "doc-en") {
		foreach (rglob("$dir/*.xml") as $filename) {
			$xml = simplexml($filename);
			if (!$xml) {
				continue;
			}
			$purpose = $xml->refnamediv->refpurpose;
			if ($purpose) {
				$translations[substr($filename, strlen($dir))] = text($purpose);
			} elseif ($xml["id"] && preg_match('~^class\.~', $xml["id"])) {
				$section = $xml->partintro->section;
				$translations[substr($filename, strlen($dir))] = text($section->para ?: $section->simpara);
			}
		}
		$dir = $enReference . $dir;
	}
	
	if (!is_dir($dir)) {
		echo "\n$dir not found";
	}
	
	$classes = array();
	foreach (rglob("$dir/*.xml") as $filename) {
		$xml = simplexml($filename);
		if (!$xml) {
			continue;
		}
		$purpose = $xml->refnamediv->refpurpose;
		$synopses = $xml->refsect1->methodsynopsis ?: $xml->refsect1->constructorsynopsis;
		if ($synopses) {
			$description = $translations[substr($filename, strlen($dir))] ?? text($purpose);
			foreach ($synopses as $synopsis) {
				$params = array();
				if ($synopsis->methodparam) {
					foreach ($synopsis->methodparam as $param) {
						$initializer = text($param->initializer);
						if ($param["choice"] == "opt" && !$initializer) {
							$initializer = "?";
						}
						if (!$param->type || $param->type == 'Type') {
							echo "\n$filename:1:missing type";
						}
						$params[] = type($param->type) . " "
							. ($param->parameter["role"] == "reference" ? "&" : "")
							. ($param["rep"] ? "..." : "")
							. "\$$param->parameter"
							. ($initializer ? " = $initializer" : "")
						;
					}
				}
				$decl = "(" . implode(", ", $params) . ")" . ($synopsis->type ? ": " . type($synopsis->type) : "");
				method($synopsis->methodname, $decl, $description, isStatic($synopsis));
			}
		} elseif ($xml->refnamediv && preg_match('~Alias ~', text($purpose))) {
			method($xml->refnamediv->refname, "()", preg_replace('~Alias ~', 'Alias of ', text($purpose)));
		} elseif ($xml["id"] && preg_match('~^class\.~', $xml["id"])) {
			$section = $xml->partintro->section;
			$classes["$xml->titleabbrev"] = $translations[substr($filename, strlen($dir))] ?? text($section->para ?: $section->simpara);
		}
	}
	foreach ($classes as $class => $purpose) {
		method("$class::new", "()", preg_replace('~\..*~', '', $purpose));
	}
}
echo "\n";

fileConstants("$enReference../appendices/tokens.xml");
foreach ($dirs as $dir) {
	foreach (glob("$enReference$dir/constants.xml") as $filename) {
		fileConstants($filename);
	}
}

preg_match_all('~^\w+~m', file_get_contents("php.api"), $matches);
$keywords = array_flip(array_map('strtolower', $matches[0]));
file_put_contents("phpfunctions.properties", 'api.$(file.patterns.php)=$(SciteDefaultHome)\php.api

statement.indent.$(file.patterns.php)=121 declare default do else elseif for foreach if switch while
statement.lookback.$(file.patterns.php)=1
block.start.$(file.patterns.php)=127 {
block.end.$(file.patterns.php)=127 }
statement.end.$(file.patterns.php)=127 ;

comment.box.start.hypertext=/*
comment.box.middle.hypertext= *
comment.box.end.hypertext= */

autocomplete.hypertext.ignorecase=1
autocomplete.hypertext.fillups=(["\'.]):;-
autocomplete.hypertext.start.characters=\\\\

calltip.hypertext.ignorecase=1
calltip.hypertext.word.characters=_$(chars.alpha)$(chars.numeric)$\\:>
calltip.hypertext.end.definition=' . SEP . '

if PLAT_WIN
	command.help.$(file.patterns.php)="https://www.php.net/$(CurrentWord)"
	command.help.subsystem.$(file.patterns.php)=2
if PLAT_GTK
	command.help.$(file.patterns.php)=chrome "https://www.php.net/$(CurrentWord)"
if PLAT_MAC
	command.help.$(file.patterns.php)=open "https://www.php.net/$(CurrentWord)"
	command.help.subsystem.$(file.patterns.php)=2

keywordclass.php=\\
'. implode(" \\\n", array_keys($keywords)) . "\n");

function isStatic($synopsis) {
	foreach ($synopsis->modifier as $modifier) {
		if ($modifier == 'static') {
			return true;
		}
	}
}

function simplexml($filename) {
	$file = file_get_contents($filename);
	$file = str_replace('xml:id=', 'id=', $file);
	$file = str_replace(' xmlns="http://docbook.org/ns/docbook"', '', $file);
	$file = preg_replace('~&([-\w.]+);~', '\1', $file);
	$return = @simplexml_load_string($file);
	if (!$return) {
		echo "\n$filename:1:parse error";
	}
	return $return;
}

function text(SimpleXMLElement $element) {
	return preg_replace('~\s+~', ' ', trim(html_entity_decode(strip_tags(str_replace('<parameter>', '$', $element->asXML())))));
}

function type(SimpleXMLElement $type) {
	$types = array();
	foreach ($type->type as $val) { // iterator_to_array() returns only the first one
		$types[] = $val;
	}
	return ($type["class"] == "union"
		? (count($types) == 2 && $types[1] == "null" ? "?$types[0]" : implode("|", $types))
		: $type
	);
}

function method($method, $decl, $purpose, $static = false) {
	static $classes = array();
	if ($static || !preg_match('~(.+)::(.+)~', $method, $match)) { // static method or normal function
		append($method . $decl . SEP . $purpose);
	} elseif ($match[2] == '__construct') { // constructor
		$classes[$match[1]] = true;
		append($match[1] . $decl . SEP . "(new) $purpose");
	} elseif ($match[2] != "new") { // method
		append(">$match[2]$decl" . SEP . "($match[1]) $purpose");
	} elseif (!array_key_exists($match[1], $classes)) { // class
		append($match[1] . $decl . SEP . "(new) $purpose");
	}
}

function fileConstants($filename) {
	$xml = simplexml($filename);
	$count = 0;
	foreach ($xml->xpath("//varlistentry") as $entry) {
		$count += termConstant($entry->term);
	}
	foreach ($xml->xpath("//row") as $row) {
		$count += termConstant($row->entry);
	}
	if (!$count) {
		echo "$filename:1:missing constants\n";
	}
}

function termConstant(SimpleXMLElement $node) {
	$constant = $node->constant;
	if ($constant) {
		append($constant);
		return 1;
	}
}

function append($s) {
	file_put_contents("php.api", "$s\n", FILE_APPEND);
}

function rglob($pattern) {
	yield from glob($pattern);
	foreach (glob(dirname($pattern) . "/*", GLOB_ONLYDIR) as $dir) {
		yield from rglob("$dir/" . basename($pattern));
	}
}
